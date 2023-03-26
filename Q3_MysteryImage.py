"""
@author: <put your name here>
"""

# TODO: implement the unmix function below


# TODO: implement the undistort_red function below


# TODO: implement the undistort_blue function below


if __name__ == '__main__':
    img = Picture("mysteryImage.png")
    img.show()
    img_red, img_blue = unmix(img)
    img_red.show()
    img_blue.show()
    undistort_red(img_red)
    img_red.show()
    undistort_blue(img_blue)
    img_blue.show()
