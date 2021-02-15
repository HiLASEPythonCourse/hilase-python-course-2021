import math

import click
import matplotlib
import skimage.io
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import rgb2gray, label2rgb


DEFAULT_THRESHOLD = 0.45
DEFAULT_SQUARE_SIZE = 5


def find_label_image(image_data, threshold=DEFAULT_THRESHOLD, square_size=DEFAULT_SQUARE_SIZE):
    # Convert to grayscale properly
    grayscale_image = rgb2gray(image_data)

    # Find mask with pixel value threshold
    binary_image = grayscale_image > threshold

    # Connect areas in a more smooth way
    smooth_image = closing(binary_image, square(square_size))

    # Clear border artifacts
    cleared_image = clear_border(smooth_image)

    # Find the labels
    label_image = label(cleared_image)

    return label_image


def report_regions(regions):
    print(f"{len(regions)} regions found.")
    print()

    for i, region in enumerate(regions):
        print(f"Region {i}")
        print(f"----------")
        print(f"  Center: {region.centroid}")
        print(f"  Area: {region.area}")
        print()


@click.group()
def run_app():
    """Universal application for finding spots in the images."""


@run_app.command()
@click.argument("path", type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.option("-t", "--threshold", type=float, default=DEFAULT_THRESHOLD, help="Threshold (0-1) to apply.")
def report(path, threshold):
    """Report spot properties."""
    image_data = skimage.io.imread(path)
    label_image = find_label_image(image_data, threshold=threshold)
    regions = regionprops(label_image)
    report_regions(regions)


@run_app.command()
@click.argument("path", type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.option("-t", "--threshold", type=float, default=DEFAULT_THRESHOLD, help="Threshold (0-1) to apply.")
@click.option("-r", "--show-regions", is_flag=True, help="Show borders around regions.")
@click.option("-e", "--show-ellipses", is_flag=True, help="Show ellipses.")
@click.option("-o", "--output", type=click.Path(), help="Output path to store the image.")
def show(path, threshold, show_regions, show_ellipses, output):
    image_data = skimage.io.imread(path)
    label_image = find_label_image(image_data, threshold=threshold)
    image_label_overlay = label2rgb(label_image, image=image_data, bg_label=0)

    matplotlib.use("TkAgg")

    # Importing here to avoid Qt problems
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(image_label_overlay)

    if show_regions:
        regions = regionprops(label_image)

        print(f"Found {len(regions)} regions.")

        for region in regions:
            # Draw rectangle around segmented spots
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                        fill=False, edgecolor='white', linewidth=2)
            ax.add_patch(rect)

    if show_ellipses:
        for region in regions:
            y0, x0 = region.centroid
            orientation = region.orientation
            x1 = x0 + math.cos(orientation) * 0.5 * region.minor_axis_length
            y1 = y0 - math.sin(orientation) * 0.5 * region.minor_axis_length
            x2 = x0 - math.sin(orientation) * 0.5 * region.major_axis_length
            y2 = y0 - math.cos(orientation) * 0.5 * region.major_axis_length

            ax.plot((x0, x1), (y0, y1), '-w', linewidth=2.5)
            ax.plot((x0, x2), (y0, y2), '-w', linewidth=2.5)
            ax.plot(x0, y0, '.w', markersize=15)

            minr, minc, maxr, maxc = region.bbox
            bx = (minc, maxc, maxc, minc, minc)
            by = (minr, minr, maxr, maxr, minr)
            #ax.plot(bx, by, '-b', linewidth=2.5)

    if output:
        fig.savefig(output)

    plt.show()


if __name__ == "__main__":
    run_app()