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

        self.OFFSET = -5
        self._angle = angle
        self._moving = False
        self.time = 0
        self._speed = 1

        self._size = size
        self._x = x
        self._y = y
        self._angle = angle
        self.bullet = pygame.Rect(
            self._x + self.OFFSET, self._y + self.OFFSET, 5, 5
        )

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    def move(self):
        """
        Moves the x & y location of the
        tank based on the angle given and
        constant speed already declared

        Args:
            direction: An int representing whether the tank is going forward or backward
        """
        self._x += self._speed * cos(radians(self._angle))
        self._y += self._speed * sin(radians(-self._angle))
        self.bullet.x = self._x
        self.bullet.y = self._y

    def moving(self, bool, x, y, angle):
        self.time = pygame.time.get_ticks()
        self._x = x + self.OFFSET
        self._y = y + self.OFFSET
        self._angle = angle
        self.bullet.x = self._x
        self.bullet.y = self._y

        self._moving = bool
