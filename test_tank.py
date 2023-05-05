"""
Tests the Tank class & its methods
Note that because it is a class we will 
need to create an instance of it for testing
purposes

"""
from math import sin, cos, radians
import pytest
import pygame
from tank import Tank


MOVE = [
    # Generic positive direction
    (1, 1),
    # Generic negative direction
    (-1, -1),
    # Double digit positive direction
    (10, 10),
    # Double digit negative direction
    (-10, -10),
    # No direction/moving
    (0, 0),
]


ANGLE = [
    # Generic Angle
    (90, 100),
    # Generic negative Angle
    (-90, -80),
    # 360  positive
    (360, 370),
    # 360 negative angle
    (-360, -350),
    # Over 360 angle
    (540, 550),
    # Over negative 360 angle
    (-540, -530),
    # No angle increase/decrease
    (0, 10),
]

ANGLE_INITIAL = [
    # Generic Angle
    (90, 90),
    # Generic negative Angle
    (-90, -90),
    # 360  positive
    (360, 360),
    # 360 negative angle
    (-360, -360),
    # Over 360 angle
    (540, 540),
    # Over negative 360 angle
    (-540, -540),
    # No angle increase/decrease
    (0, 0),
]

COORD = [
    # Origin
    ((0, 0), (0, 0)),
    # Positive Coord
    ((10, 10), (10, 10)),
    # Negative Coord
    ((-10, -10), (-10, -10)),
    # Negative X
    ((-10, 10), (-10, 10)),
    # Negative Y
    ((10, -10), (10, -10)),
]


COORD_ANGLED = [
    # Origin
    ((0, 0), (0 + cos(radians(45)), 0 + sin(radians(-45)))),
    # Positive Coord
    ((10, 10), (10 + cos(radians(45)), 10 + sin(radians(-45)))),
    # Negative Coord
    ((-10, -10), (-10 + cos(radians(45)), -10 + sin(radians(-45)))),
    # Negative X
    ((-10, 10), (-10 + cos(radians(45)), 10 + sin(radians(-45)))),
    # Negative Y
    ((10, -10), (10 + cos(radians(45)), -10 + sin(radians(-45)))),
]


@pytest.mark.parametrize("dir, key", MOVE)
def test_move_dir(dir, key):
    """We test whether we are able to save our last direction to
    be the last direction after a running the move function

    Args:
        dir: An int that symbolizes the dir
        key: An int which is the correct last direction.
    """
    tank = Tank((150, 250), pygame.sprite.Group(), 2)

    tank.move(dir)
    assert tank.lastdir == key


@pytest.mark.parametrize("angle, key", ANGLE)
def test_angle(angle, key):
    """We test whether we are able to rotate our tank by an angle.
    Our tank is initialized at an angle of 10, so after rotation,
    our angle should be the angle + 10 degrees

    Args:
        angle: An int that symbolizes the dengree angle to change by
        key: An int which is the correct total angle.
    """
    tank = Tank((150, 250), pygame.sprite.Group(), 2, 10)

    print(tank.angle)

    tank.rotate(angle)
    print(tank.angle)
    assert tank.angle == key


@pytest.mark.parametrize("angle, key", ANGLE_INITIAL)
def test_initialize_angle(angle, key):
    """We test whether we are able to initialize our tank at an angle.

    Args:
        angle: An int that symbolizes the degree angle
        the tank initially faces
        key: An int which is the correct total angle.
    """
    tank = Tank((150, 250), pygame.sprite.Group(), 2, angle)

    assert tank.angle == key


@pytest.mark.parametrize("coord, key", COORD)
def test_xy(coord, key):
    """We test whether we initialize our x & y
    in the right coordinates

    Args:
        coord: A tuple that symbolizes the x y int location
        of the tank
        key: A tuple which is the correct x y int location.
    """
    tank = Tank(coord, pygame.sprite.Group(), 2)

    assert tank.tank_x == key[0] and tank.tank_y == key[1]


@pytest.mark.parametrize("coord, key", COORD_ANGLED)
def test_xy_rotate(coord, key):
    """We test whether we move to the correct location
    with an angle of 45 degrees

    Args:
        coord: An tuple that symbolizes the x y int location
        of the tank initially
        key: A tuple which is the correct x y coord given
        the tank is facing  at 45 degrees.
    """
    tank = Tank(coord, pygame.sprite.Group(), 1, 45)

    tank.move(1)

    assert tank.tank_x == key[0] and tank.tank_y == key[1]
