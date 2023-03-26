"""
@author: <put your name here>
"""

from imageTools import *

def average_color(pic: Picture, x0: int, y0: int, size: int) -> ImageColor:
    """
    Compute the average color for a portion of given picture specified by a
    square of a give size placed at the given location

    @param pic: a picture object
    @param x0: the x-coordinate of the upper-left corner of the square
    @param y0: the y-coordinate of the upper-left corner of the square
    @param size: the size of the square
    @return: average color of the portion of the picture specified by the square
    """
    wid = pic.getWidth()
    hgt = pic.getHeight()
    sum_r = 0
    sum_g = 0
    sum_b = 0
    pix_count = 0
    for x in range(x0, x0+size):
        for y in range(y0, y0+size):
            if (0 <= x < wid) and (0 <= y < hgt):
                (r, g, b) = pic.getColor(x, y)
                sum_r += r
                sum_g += g
                sum_b += b
                pix_count += 1
    return sum_r // pix_count, sum_g // pix_count, sum_b // pix_count


# TODO: implement the mosaic function below
