"""
@author: <put your name here>
"""

from util.imageTools import *
from util.display_helper import *

# TODO: implement the unmix function below


# TODO: implement the undistort_red function below


# TODO: implement the undistort_blue function below


def main():
    img = Picture("mysteryImage.png")
    display_images([img])

    img_red, img_blue = unmix(img)
    display_images([img_red, img_blue])

    undistort_red(img_red)
    undistort_blue(img_blue)
    scene = Picture("theCrimeScene.png")
    culprit = Picture("theCulprit.png")
    display_images([scene, culprit])


if __name__ == '__main__':
    main()
