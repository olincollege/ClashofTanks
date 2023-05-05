"""Contains the Tank class"""
from math import sin, cos, radians
import pygame


class Tank(pygame.sprite.Sprite):
    """A pygame sprite subclass that represents the
    tanks in the Atari 2600 Combat game

    Attributes:
        offset: an int that determines the offset of the hitbox
        from the Tank sprite image
        lastdir: an int that keeps track of the last direction
        the tank faced
    """

    def __init__(self, pos, groups, speed, angle=0):
        """
            Initializes the Tank object
        Args:
            pos: a tuple that contains the x & y coordinates of
            the sprite's initialization location.
            groups: A pygame.sprite.Group() object which determines
            which group the Tank sprite will be in
            speed: An int that determines the initial speed
            of the tank
            angle: an int that determines the angle the
            sprite is facing in degrees
        """

        super().__init__(groups)

        self.offset = -20
        self._angle = angle
        self.lastdir = 1

        self._x = pos[0]
        self._y = pos[1]
        self._speed = speed
        self._hitbox = pygame.Rect(
            self._x + self.offset, self._y + self.offset, 37, 37
        )

    # Getter Methods
    @property
    def tank_x(self):
        """
        Return:
            The int _x variable
        """
        return self._x

    @property
    def tank_y(self):
        """
        Return:
            The int _y variable
        """
        return self._y

    @property
    def hitbox(self):
        """
        Return:
            The int _hitbox variable
        """
        return self._hitbox

    @property
    def angle(self):
        """
        Return:
            The int _angle variable
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """
        sets the value of _angle
        to a new value

        Args:
            angle: An int value
        """
        self._angle = angle

    @property
    def speed(self):
        """
        Return:
            The int _speed variable
        """
        return self._speed

    def move(self, direction):
        """
        Moves the x & y location of the
        tank based on the angle given and
        constant speed already declared

        Args:
            direction: An int representing whether
            the tank is going forward or backward
        """
        self.lastdir = direction
        self._x += direction * self._speed * cos(radians(self._angle))
        self._y += direction * self._speed * sin(radians(-self._angle))

        self._hitbox.x = self._x + self.offset
        self._hitbox.y = self._y + self.offset

    def rotate(self, angle):
        """Updates the angle of the tank
        by a specific degree

        Args:
            angle: An int that represents the angle
            in degrees
        """
        self._angle += angle
