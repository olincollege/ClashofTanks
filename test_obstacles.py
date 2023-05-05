"""
Tests the obstacles class & its methods
Note that because it is a class we will
need to create an instance of it for testing
purposes

There are also no unit tests for internal
helper functions that only use the function draw()
(map1, map2) because we have unit tests for the draw
function and the internal helper functions don't have
any parameters. Hence it's pointless to have unit
tests for these internal helper functions if we
have unit tests for the draw() function. There
are also no unit tests for @property.

"""
import pytest
import pygame
from obstacles import Obstacles


DRAW = [
    # Draws in correct location
    ([10, 5], pygame.Rect),
    # Draws in correct location, last index
    ([39, 19], pygame.Rect),
    # Draws in correct location, first index
    ([0, 0], pygame.Rect),
    # Doesn't accept negative indexes
    ([-2, -2], int),
    # Doesn't accept out of bounds
    ([-45, -100], IndexError),
    # Doesn't accept strings
    ([10, "hello"], TypeError),
    # Doesn't accept floats
    ([10, 0.5], TypeError),
]

LAYOUT = [
    # Testing filled index
    ([0, 0], pygame.Rect(0, 0, 25, 25)),
    # Testing empty index
    ([3, 3], 0),
    # Testing filled index
    ([0, 4], pygame.Rect(0, 4 * 25, 25, 25)),
]


@pytest.mark.parametrize("coord, key", DRAW)
def test_draw(coord, key):
    """We test whether we were able to write to correct index
    using the draw data

    Args:
        coord: A list with a length of 2. The first index contains
        the x coordinate,the second index contains the y coordinate.
        Each index does not have to be an int, but it generally is.
        key: A type (pygame.Error, Exception) which indicates whether
        the index was filled or what error is returned.
    """
    obstacle = Obstacles(0)

    obstacle.draw(coord[0], coord[1])

    # IF something was written successfully
    try:
        assert isinstance(obstacle.layout[coord[1]][coord[0]]) == key
    # If error thrown, should be error we're expecting
    except TypeError as exc:
        assert isinstance(exc) == key
    except IndexError as exc:
        assert isinstance(exc) == key


@pytest.mark.parametrize("coord, key", LAYOUT)
def test_layout(coord, key):
    """We test whether layout saves the correct information

    Args:
        coord: A list with a length of 2. The first index contains
        the x coordinate, the second index contains the y coordinate.
        Each index does not have to be an int, but it generally is.
        key: A pygame.Rect or int which indicates what the index
        should contain
    """

    obstacle = Obstacles(0)

    assert obstacle.layout[coord[1]][coord[0]] == key
