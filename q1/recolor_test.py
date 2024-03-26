"""
A set of unit tests for the functions in recolor module

@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""

from recolor import find_closest_color


def test_fcc_one_color_list() -> None:
    """
    Test when the list contains only one color
     
    @return: None 
    """
    color = (100, 100, 100)
    color_list = [(5, 5, 5)]

    actual = find_closest_color(color, color_list)
    expected = color_list[0]

    assert actual == expected


def test_fcc_exact_color_exist() -> None:
    """
    Test when the list contains exact match of the color
    
    @return: None 
    """
    color = (100, 100, 100)
    color_list = [(101, 100, 100), color, (100, 100, 101)]

    actual = find_closest_color(color, color_list)
    expected = color

    assert actual == expected


def test_fcc_closest_color_first() -> None:
    """
    Test when the closest color is first in the list

    @return: None
    """
    color = (10, 10, 10)
    color_list = [(5, 5, 5), (50, 50, 50), (100, 100, 100)]

    actual = find_closest_color(color, color_list)
    expected = color_list[0]

    assert actual == expected


def test_fcc_closest_color_last() -> None:
    """
    Test when the closest color is last in the list

    @return: None
    """
    color = (10, 10, 10)
    color_list = [(50, 50, 50), (100, 100, 100), (5, 5, 5)]

    actual = find_closest_color(color, color_list)
    expected = color_list[2]

    assert actual == expected


def test_fcc_closest_color_middle() -> None:
    """
    Test when the closest color is the middle of the list

    @return: None
    """
    color = (10, 10, 10)
    color_list = [(50, 50, 50), (5, 5, 5), (100, 100, 100)]

    actual = find_closest_color(color, color_list)
    expected = color_list[1]

    assert actual == expected
