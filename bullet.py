"""Bullet Class of the Combat game"""
from math import sin, cos, radians
import pygame


class Bullet(pygame.sprite.Sprite):
    """
    A Bullet Class which is a pygame Sprite subclass
    that represents the bullet/shell f0ired by the
    tank in the game Combat.

    Attributes:
        OFFSET: An int value that controls the offset
        of the bullet's location from the tank's center
        time: An int value that keeps track of how
        long the bullet has been moving.
        bullet: A pygame Rectangle object that represents
        the rectangle property of the bullet.
        moving: A boolean that is True if the bullet is moving
        and False if not moving

    """

    def __init__(self, groups, loc, angle, size=5):
        """Initialization function for the Bullet Class

        Args:
            groups: a pygame.sprite.Group(). Identifies which
            group this object will be part of.
            loc: an tuple containing 2 int value which is the x & y
            location of the bullet
            angle: an int value which represents the degree the bullet
            is facing
            size: An optional int parameter which determines the size of
            the bullet

        """
        super().__init__(groups)

        self._angle = angle
        self.is_moving = False
        self.time = 0
        self._speed = 0.5

        self._x = loc[0]
        self._y = loc[1]
        self.bullet = pygame.Rect(self._x - 5, self._y - 5, size, size)

    @property
    def angle(self):
        """
        Return:
            An int _angle attribute"""
        return self._angle

    @angle.setter
    def angle(self, value):
        """Sets the _angle to a new value

        Arg:
            value: an int value representing a
            degree"""
        self._angle = value

    def move(self):
        """
        Moves the x & y location of the
        tank based on the angle given and
        constant speed already declared
        """
        self._x += self._speed * cos(radians(self._angle))
        self._y += self._speed * sin(radians(-self._angle))
        self.bullet.x = self._x
        self.bullet.y = self._y

    def moving(self, moving, loc, angle):
        """A function that sets the different
        internal and external attributes

        Args:
            moving: a boolean value to set
            the value of the _moving attribute
            loc: a tuple containing 2 int value to set the
            value of the x & y attribute
            angle: an int value to set the _angle
            attribute to a new degree
        """
        self.time = pygame.time.get_ticks()
        self._x = loc[0] - 5
        self._y = loc[1] - 5
        self._angle = angle
        self.bullet.x = self._x
        self.bullet.y = self._y

        self.is_moving = moving

        if moving:
            pygame.mixer.Sound.play(pygame.mixer.Sound("audio/shooting.wav"))
            pygame.mixer.music.stop()

    def ricochet(self):
        """A function that simulates the ricochet
        behavior of a bullet when it bounces off obstacles
        by changing the direction of the bullet's trajectory"""
        self._angle = 160 + self._angle
