"""
Unit tests for the obstacles class & its methods
Note that because it is a class we will
need to create an instance of it for testing
purposes

There are also no unit tests for @property.

"""
# pylint: disable-all

import pytest
import pygame
from obstacles import Obstacles


DRAW = [
    # Draws in the correct location
    ([10, 5], pygame.Rect),
    # Draws in the correct location, last index
    ([39, 19], pygame.Rect),
    # Draws in the correct location, first index
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
    # Test Layout 1
    (
        0,
        [
            (10, 7),
            (10, 8),
            (10, 9),
            (10, 10),
            (10, 11),
            (10, 12),
            (9, 7),
            (8, 7),
            (9, 12),
            (8, 12),
            (3, 3),
            (3, 4),
            (3, 17),
            (3, 16),
            (19, 10),
            (19, 12),
            (19, 13),
            (19, 7),
            (19, 9),
            (19, 6),
        ],
    ),
    # Test Layout 2
    (
        1,
        [
            (10, 7),
            (10, 12),
            (9, 7),
            (8, 7),
            (9, 12),
            (8, 12),
            (3, 3),
            (3, 4),
            (3, 17),
            (3, 16),
        ],
    ),
    # Test Layout 3
    (
        2,
        [
            (10, 7),
            (10, 12),
            (9, 7),
            (8, 7),
            (9, 12),
            (8, 12),
            (3, 3),
            (3, 4),
            (3, 17),
            (3, 16),
            (15, 10),
            (15, 11),
            (15, 9),
            (17, 1),
            (17, 18),
        ],
    ),
    # Test Layout 4
    (
        3,
        [
            (10, 7),
            (10, 8),
            (10, 9),
            (10, 10),
            (10, 11),
            (10, 12),
            (9, 7),
            (8, 7),
            (9, 12),
            (8, 12),
            (3, 3),
            (3, 4),
            (3, 17),
            (3, 16),
            (19, 10),
            (19, 12),
            (19, 13),
            (19, 7),
            (19, 9),
            (19, 6),
            (15, 10),
            (15, 11),
            (15, 9),
            (17, 1),
            (17, 18),
        ],
    ),
    (
        4,
        [
            (8, 12),
            (3, 3),
            (15, 3),
            (15, 6),
            (15, 7),
            (15, 4),
            (15, 2),
            (14, 6),
            (14, 7),
            (16, 6),
            (16, 7),
            (16, 5),
            (16, 4),
            (15, 17),
            (15, 14),
            (15, 13),
            (15, 16),
            (14, 14),
            (14, 13),
            (16, 14),
            (16, 13),
            (16, 15),
            (16, 16),
            (3, 17),
            (8, 11),
            (8, 10),
            (8, 9),
            (8, 8),
        ],
    ),
]


@pytest.mark.parametrize("coord, key", DRAW)
def test_draw(coord, key):
    """We test whether we were able to write to correct index
    using the draw data

    Args:
        coord: A list with a length of 2. The first index contains
        the x coordinate, the second index contains the y coordinate.
        Each index does not have to be an int, but it generally is.
        key: A type (pygame.Error, Exception) that indicates whether
        the index was filled or what error is returned.
    """
    obstacle = Obstacles(0)

    obstacle.draw(coord[0], coord[1])

    # IF something was written successfully
    try:
        assert isinstance(obstacle.layout[coord[1]][coord[0]], key)
    # If error thrown, should be error we're expecting
    except TypeError as exc:
        assert isinstance(exc, key)
    except IndexError as exc:
        assert isinstance(exc, key)


@pytest.mark.parametrize("layout, coord", LAYOUT)
def test_layout(layout, coord):
    """We test whether the layout saves the correct information

    Args:
        coord: A list with tuples nested in the index with a length of 2.
        The first index contains the x coordinate, the second index
        contains the y coordinate.

        layout: A int which indicates what the layout
        obstacle it should be
    """

    obstacle = Obstacles(layout)

    for loc in coord:
        print(loc)
        print(obstacle.layout[loc[1]][loc[0]])
        # Check it works
        assert obstacle.layout[loc[1]][loc[0]] == pygame.Rect(
            loc[0] * 25, loc[1] * 25, 25, 25
        )
        # Check Mirroring
        assert obstacle.layout[loc[1]][1000 // 25 - 1 - loc[0]] == pygame.Rect(
            (1000 // 25 - 1 - loc[0]) * 25, loc[1] * 25, 25, 25
        )
