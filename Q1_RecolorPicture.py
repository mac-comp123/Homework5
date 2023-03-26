"""
@author: <put your name here>
"""

from imageTools import *


# TODO: implement the find_closest_color function below
def find_closest_color(color: ImageColor,
                       color_list: list[ImageColor]) -> ImageColor:
    pass


# TODO: implement the recolor function below
def recolor(pic: Picture,
            color_list: list[ImageColor]) -> Picture:
    pass


if __name__ == "__main__":
    color_list1 = ["green", "maroon", "black", "red"]
    color_list2 = ["lime", (76, 133, 16),  # dark green
                   (166, 237, 90),  # light green
                   (240, 128, 128),  # light coral
                   (135, 206, 250),  # light sky blue
                    "white", "black", "blue"]
    color_list3 = ["coral", "white", "blue"]

    snow = Picture("SampleImages/snow.jpg")
    butterfly = Picture("SampleImages/butterfly.jpg")
    skaters = Picture("SampleImages/landmarkSkaters.jpg")
    snow_recolored = recolor(snow, color_list1)
    butterfly_recolored = recolor(butterfly, color_list2)
    skaters_recolored = recolor(skaters, color_list3)
    snow_recolored.show()
    butterfly_recolored.show()
    skaters_recolored.show()
