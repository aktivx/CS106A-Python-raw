"""
File: ghost.py
--------------
ADD YOUR DESCRIPTION HERE
"""


import os
import sys


# The line below imports SimpleImage for use here.
# It depends on the Pillow package being installed.
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    # Your code goes here
    pixel_dist = (pixel.red - red) ** 2 + (pixel.green - green) ** 2 + (pixel.blue - blue) ** 2
    return pixel_dist


def get_best_pixel(pixel1, pixel2, pixel3):
    """
    Given three pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        three pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel(green_pixel, blue_pixel, blue_pixel)
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel(green_pixel, green_pixel, blue_pixel)
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel(red_pixel, red_pixel, red_pixel)
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    # Your code goes here
    red_avg = (pixel1.red + pixel2.red + pixel3.red) // 3
    green_avg = (pixel1.green + pixel2.green + pixel3.green) // 3
    blue_avg = (pixel1.blue + pixel2.blue + pixel3.blue) // 3
    pixel1_dist = get_pixel_dist(pixel1, red_avg, green_avg, blue_avg)
    pixel2_dist = get_pixel_dist(pixel2, red_avg, green_avg, blue_avg)
    pixel3_dist = get_pixel_dist(pixel3, red_avg, green_avg, blue_avg)
    smallest_pixel_dist = smallest_number(pixel1_dist, pixel2_dist, pixel3_dist)
    if smallest_pixel_dist == pixel1_dist:
        return pixel1
    elif smallest_pixel_dist == pixel2_dist:
        return pixel2
    else:
        return pixel3

def smallest_number(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3


def create_ghost(image1, image2, image3):
    """
    Given three image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        three images to be processed
    Returns:
        a new Ghost solution image
    """
    # Your code goes here
    width = image1.width
    height = image1.height
    ghost_image = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel_image1 = image1.get_pixel(x,y)
            pixel_image2 = image2.get_pixel(x,y)
            pixel_image3 = image3.get_pixel(x,y)
            best_pixel = get_best_pixel(pixel_image1, pixel_image2, pixel_image3)
            ghost_image.set_pixel(x, y, best_pixel)
    return ghost_image


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images[0], images[1], images[2])
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")

if __name__ == '__main__':
    main()
