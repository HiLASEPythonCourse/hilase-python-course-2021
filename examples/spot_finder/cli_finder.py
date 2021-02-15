import sys

import skimage.io
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import rgb2gray


DEFAULT_THRESHOLD = 0.45
DEFAULT_SQUARE_SIZE = 5


def find_regions(path, threshold=DEFAULT_THRESHOLD, square_size=DEFAULT_SQUARE_SIZE):
    # Read it
    original_image = skimage.io.imread(path)

    # Convert to grayscale properly
    grayscale_image = rgb2gray(original_image)

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
    for i, region in enumerate(regions):
        print(f"Region {i}")
        print(f"----------")
        print(f"  Center: {region.centroid}")
        print(f"  Area: {region.area}")
        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input("Name of the file? ")
    regions = find_regions(file_name)
    report_regions(regions)