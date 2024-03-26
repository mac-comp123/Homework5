"""
@author: <put your name here>
"""
from util.display_helper import *
from util.imageTools import *


# TODO: implement the find_closest_color function below
def find_closest_color(color: ImageColor,
                       color_list: list[ImageColor]) -> ImageColor:
    ...


# TODO: implement the recolor function below
def recolor(pic: Picture,
            color_list: list[ImageColor]) -> Picture:
    ...


def main():
    color_list1 = ["green", "maroon", "black", "red"]
    snow = Picture("../SampleImages/snow.jpg")
    snow_recolored = recolor(snow, color_list1)
    display_images([snow, snow_recolored])

    color_list2 = ["lime", (76, 133, 16),  # dark green
                   (166, 237, 90),  # light green
                   (240, 128, 128),  # light coral
                   (135, 206, 250),  # light sky blue
                   "white", "black", "blue"]
    butterfly = Picture("../SampleImages/butterfly.jpg")
    butterfly_recolored = recolor(butterfly, color_list2)
    display_images([butterfly, butterfly_recolored])

    color_list3 = ["coral", "white", "blue"]
    skaters = Picture("../SampleImages/landmarkSkaters.jpg")
    skaters_recolored = recolor(skaters, color_list3)
    display_images([skaters, skaters_recolored])


if __name__ == "__main__":
    main()
