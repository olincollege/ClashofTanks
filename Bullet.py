"""Bullet"""

import pygame
from math import sin, cos, radians


class Bullet(pygame.sprite.Sprite):
    """
    Args:
        pos: a tuple that contains the x & y coordinates of
        the sprite's initalization location.
        image: A string which is the path to the image we'll be using

        *groups: a pygame.sprite.Group(). Identifies which
        group this object will be part of."""

    def __init__(self, groups, x, y, angle, size=10):
        super().__init__(groups)
        self._size = size
        self._x = x
        self._y = y
        self._angle = angle

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move(self, direction):
        """
        Moves the x & y location of the
        tank based on the angle given and
        constant speed already declared

        Args:
            direction: An int representing whether the tank is going forward or backward
        """
        self._x += direction * self._speed * cos(radians(self._angle))
        self._y += direction * self._speed * sin(radians(-self._angle))
