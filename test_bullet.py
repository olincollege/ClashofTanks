"""
Tests the Bullet class & its methods
Note that because it is a class we will
need to create an instance of it for testing
purposes.

"""
from math import sin, cos, radians
import pytest
import pygame
from bullet import Bullet

RICOCHET = [
    # Generic Angle
    (90, 250),
    # Generic negative Angle
    (-90, 70),
    # 360  positive
    (360, 520),
    # 360 negative angle
    (-360, -200),
    # Over 360 angle
    (540, 700),
    # Over negative 360 angle
    (-540, -380),
    # No angle increase/decrease
    (0, 160),
]


MOVE = [
    # All Unit Circle Angles
    (0, (0.5 * cos(radians(0)), (0.5 * sin(radians(-0))))),
    (30, (0.5 * cos(radians(30)), (0.5 * sin(radians(-30))))),
    (45, (0.5 * cos(radians(45)), (0.5 * sin(radians(-45))))),
    (90, (0.5 * cos(radians(90)), (0.5 * sin(radians(-90))))),
    (120, (0.5 * cos(radians(120)), (0.5 * sin(radians(-120))))),
    (135, (0.5 * cos(radians(135)), (0.5 * sin(radians(-135))))),
    (150, (0.5 * cos(radians(150)), (0.5 * sin(radians(-150))))),
    (180, (0.5 * cos(radians(180)), (0.5 * sin(radians(-180))))),
    (210, (0.5 * cos(radians(210)), (0.5 * sin(radians(-210))))),
    (225, (0.5 * cos(radians(225)), (0.5 * sin(radians(-225))))),
    (240, (0.5 * cos(radians(240)), (0.5 * sin(radians(-240))))),
    (270, (0.5 * cos(radians(270)), (0.5 * sin(radians(-270))))),
    (300, (0.5 * cos(radians(300)), (0.5 * sin(radians(-300))))),
    (315, (0.5 * cos(radians(315)), (0.5 * sin(radians(-315))))),
    (330, (0.5 * cos(radians(330)), (0.5 * sin(radians(-330))))),
    (360, (0.5 * cos(radians(360)), (0.5 * sin(radians(-360))))),
]

MOVING = [
    # Origin
    ((0, 0), (-5, -5)),
    # Positive
    ((1, 1), (-4, -4)),
    # Negative
    ((-1, -1), (-6, -6)),
    # Large Positive
    ((10, 10), (5, 5)),
]


@pytest.mark.parametrize("angle, key", RICOCHET)
def test_ricochet(angle, key):
    """We test whether the bullet can ricochet properly by
    changing directions
    Args:
        angle: An int with the initial angle of the bullet
        key: An int with the new angle of the bullet
        after ricochetting.
    """
    bullet = Bullet(pygame.sprite.Group(), (0, 0), angle)
    bullet.ricochet()

    assert bullet.angle == key


@pytest.mark.parametrize("angle, key", MOVE)
def test_move(angle, key):
    """We test whether the bullet can move properly
    given different angles
    Args:
        angle: an int angle in degrees that the bullet
        will be facing
        key: A tuple with 2 integers which represent
        the (x,y) coord respectively after one move.
    """
    test_bullet = Bullet(pygame.sprite.Group(), (0, 0), angle)
    test_bullet.move()

    assert test_bullet.bullet_x == key[0] and test_bullet.bullet_y == key[1]


@pytest.mark.parametrize("loc, key", MOVING)
def test_moving(loc, key):
    """We test whether the after moving the values of x & y
    have been correctly set through the moving function
    with account for offset (Which is -5).
    Args:

        loc: A tuple with 2 intege  rs which represent
        the (x,y) coord respectively.
        key: loc: A tuple with 2 integers which represent
        the (x,y) coord respectively after moving.
    """
    test_bullet = Bullet(pygame.sprite.Group(), (0, 0), 0)
    test_bullet.moving(False, loc, 0)

    assert test_bullet.bullet_x == key[0] and test_bullet.bullet_y == key[1]
