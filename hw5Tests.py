""" =======================================================================
    File: hw5Tests.py
    Name:

    Contains test function for findClosestColor function of Homework 5.

    ===========================================================================
"""

from hw5Code import *

def test_FindClosestColor():
    """Tests the findClosestColor function by making a series of calls
    and checking that the returned value is as expected."""


    colors1 = ["red", "lime", "blue", "yellow", "pink", "white", "black",
                 "purple", "orange"]
    colors2 = ["lime", (76, 133, 16),  # dark green
                   (166, 237, 90),  # light green
                   (240, 128, 128),  # light coral
                   (135, 206, 250),  # light sky blue
                   "white", "black", "blue"]

    # Test 1
    c1 = findClosestColor((240, 15, 30), colors1)
    assert c1 == "red"

    ## --- add more tests like the one above, using both colors1 and colors2, as well
    ## --- as additional color lists of your own making.

def runTests():
    print("BEGIN TESTING")
    test_FindClosestColor()
    print()
    print("DONE WITH ALL TESTS.")

runTests()