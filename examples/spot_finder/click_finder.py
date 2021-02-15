import click

import skimage.io
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import rgb2gray


DEFAULT_THRESHOLD = 0.45
DEFAULT_SQUARE_SIZE = 5


def find_regions(image_data, threshold=DEFAULT_THRESHOLD, square_size=DEFAULT_SQUARE_SIZE):
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

    # Computer properties for the labels
    return regionprops(label_image)


def report_regions(regions):
    print(f"{len(regions)} regions found.")
    print()

    for i, region in enumerate(regions):
        print(f"Region {i}")
        print(f"----------")
        print(f"  Center: {region.centroid}")
        print(f"  Area: {region.area}")
        print()


@click.command()
@click.argument("path", type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.option("-t", "--threshold", type=float, default=DEFAULT_THRESHOLD, help="Threshold (0-1) to apply.")
def run_app(path, threshold):
    """Find spots in an image."""
    image_data = skimage.io.imread(path)
    regions = find_regions(image_data, threshold=threshold)
    report_regions(regions)


if __name__ == "__main__":
    run_app()