"""
@author: <put your name here>
"""

from util.imageTools import *
from util.display_helper import *


# TODO: implement the rotate_pic function below


def main():
    eagle = Picture("../SampleImages/baldEagle.jpg")
    eagle45 = rotate_pic(eagle, 45)
    eagle60 = rotate_pic(eagle, 60)
    display_images([eagle, eagle45, eagle60])

    astilbe = Picture("../SampleImages/astilbe.jpg")
    astilbe_33 = rotate_pic(astilbe, -33)
    astilbe10 = rotate_pic(astilbe, 10)
    display_images([astilbe, astilbe_33, astilbe10])


if __name__ == '__main__':
    main()
