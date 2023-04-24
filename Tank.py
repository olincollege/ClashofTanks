"""Contains the Tank class"""

import pygame
from math import sin, cos


class Tank(pygame.sprite.Sprite):
    def __init__(self, pos, groups, health, speed):
        """
            Initializes the Tank object
        Args:
            pos: a tuple that contains the x & y coordinates of
            the sprite's initialization location.
            groups: A pygame.sprite.Group() object which determines
            which group the Tank sprite will be in
            health: An int which determines the initial health
            of the tank
            speed: An int that determines the intitial speed
            of the tank
        """

        super().__init__(groups)

        self.OFFSET = 20

        self._x = pos[0]
        self._y = pos[1]
        self._health = health
        self._speed = speed
        self._hitbox = pygame.Rect(
            self._x + self.OFFSET, self._y + self.OFFSET, 20, 20
        )  # A rectangle object that functions as a hitbox. Useful for rect.collide

    # Getter Methods
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def hitbox(self):
        return self._hitbox

    def move(self, angle):
        """
        Moves the x & y location of the
        tank based on the angle given and
        constant speed already declared

        Args:
            angle: An int representing the degree
            the Tank is facing
        """
        self._x += self._speed * cos(angle)
        self._y += self._speed * sin(angle)
