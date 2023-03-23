""" =======================================================================
    File: hw5Code.py
    Name:

    Contains solutions and test calls for Homework 5.

    ===========================================================================
"""
# =============================
# Import section

from imageTools import *
import string


# =============================
# Function definition section


# -------------------------------------------------------------------------
# Question 1 - testing findClosestColor

def findClosestColor(newColor, colorList):
    """Takes in a color object and a list of color objects. It compares newColor
    to each color in the colorList, and keeps track of the most similar color
    from the color list (the one where distance is smallest). It returns the
    most similar color from the colorList."""
    currClosest = colorList[0]
    currDist = distance(newColor, currClosest)
    for col in colorList:
        nextDist = distance(newColor, col)
        if nextDist < currDist:
            currClosest = col
            currDist = nextDist
    return currClosest

# TODO: Put your tests in the testing file

# -------------------------------------------------------------------------
# Question 2 - simplify

# TODO: Put your definition of simplify here

# -------------------------------------------------------------------------
# Question 3 - xraySquare

# TODO: Put your definition of xraySquare here

# -------------------------------------------------------------------------
# Question 4 - mysteryImage

# TODO: Put your definition of unmix, undistortedRed, and undistortedBlue here

# -------------------------------------------------------------------------
# Question 5 - varyBlend

def weightedBlend(pic1, pic2, wgt1):
    wgt2 = 1 - wgt1
    width1 = pic1.getWidth()
    height1 = pic1.getHeight()
    width2 = pic2.getWidth()
    height2 = pic2.getHeight()
    width = min(width1, width2)
    height = min(height1, height2)
    newPic = Picture(width, height)
    for x in range(width):
        for y in range(height):
            (r1, g1, b1) = pic1.getColor(x, y)
            (r2, g2, b2) = pic2.getColor(x, y)
            newRed = wgt1 * r1 + wgt2 * r2
            newGreen = wgt1 * g1 + wgt2 * g2
            newBlue = wgt1* b1 + wgt2 * b2
            newPic.setColor(x, y, (newRed, newGreen, newBlue))
        newPic.show()
    return newPic

# TODO: Put your definition of varyBlend here




# ----------------------------------------------------------------------

if __name__ == '__main__':
    print("Tests...")

    # Sample calls for Question 2: simplify
    '''
    testColors1 = ["green", "maroon", "black", "red"]
    testColors2 = ["lime", (76, 133, 16),  # dark green
                (166, 237, 90),  # light green
                (240, 128, 128),  # light coral
                (135, 206, 250),  # light sky blue
                "white", "black", "blue"]
    testColors3 = ["coral", "white", "blue"]
    
    p1 = Picture("SampleImages/snow.jpg")
    p2 = Picture("SampleImages/butterfly.jpg")
    p3 = Picture("SampleImages/landmarkSkaters.jpg")
    newP1 = simplify(p1, testColors1)
    newP2 = simplify(p2, testColors2)
    newP3 = simplify(p3, testColors3)
    newP1.show()
    newP2.show()
    newP3.show()
    '''

    # Sample calls to Question 3: xraySquare
    '''
    p4 = Picture("SampleImages/bristleconePine.jpg")
    midx = p4.getWidth() // 2  # find midpoint of picture
    midy = p4.getHeight() // 2
    xraySquare(p4, 10, 10, 50)  # small upper left
    xraySquare(p4, midx, midy, 300)  # large center/lower right
    xraySquare(p4, 10, 200, 100)  # medium middle/left
    p4.show()
    '''

    # Sample calls for Question 4: mystery Image
    '''
    p5 = Picture("mysteryImage.png")
    p5.show()
    p6, p7 = unmix(p5)
    p6.show()
    p7.show()
    undistortRed(p6)
    p6.show()
    undistortBlue(p7)
    p7.show()
    '''

    # Sample calls for Question 5: varyBlend
    '''
    p8 = Picture("SampleImages/glacierOldBurn2.jpg")
    p9 = Picture("SampleImages/selbyWinter.jpg")
    p10 = Picture("SampleImages/redMushroom.jpg")
    p11 = Picture("SampleImages/raspberries.jpg")
    
    w1 = weightedBlend(p8, p9, .5)
    w1.show()
    
    b1 = varyBlend(p8, p9)
    b1.show()
    b2 = varyBlend(p9, p8)
    b2.show()
    b3 = varyBlend(p10, p11)
    b3.show()
    b4 = varyBlend(p11, p10)
    b4.show()
    '''

