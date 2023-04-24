"""Bullet"""

import pygame


class Bullet(pygame.sprite.Sprite):
    """
    Args:
        pos: a tuple that contains the x & y coordinates of
        the sprite's initalization location.
        image: A string which is the path to the image we'll be using

        *groups: a pygame.sprite.Group(). Identifies which
        group this object will be part of."""

    def __init__(self, size, *groups):
        super().__init__(*groups)
        self._size = size

    @property
    def size(self):
        return self._size
