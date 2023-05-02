"""Obstacles Class of the Combat game """

import pygame


class Obstacles:
    """A Obstacles Class which generates obstacle rectangles
    and the different layouts

    Attributes:
        size: size of each rectangle
    """

    def __init__(self, map_type):
        """Initializes the obstacles class

        Args:
            map_type: An int that determines the map layout type
        """

        self.size = 25
        # generates an list with 0s which is a matrix where each
        #  index represents a grid location on the screen
        self._layout = [
            [0 for i in range(1000 // self.size)]
            for i in range(500 // self.size)
        ]

        # Makes the border
        self.border()
        # Select layout type
        if map_type == 1:
            self.map1()
        if map_type == 2:
            pass

    @property
    def layout(self):
        """Return:
        a list of the instance attribute _layout"""
        return self._layout

    def draw(self, xpara, ypara):
        """updates an index with the corresponding
        rectangle

        Args:
            x: an int value
            y: an int value
        """
        self._layout[ypara][xpara] = pygame.Rect(
            xpara * self.size, ypara * self.size, self.size, self.size
        )

    # Helper Functions
    def border(self):
        """Draws a border by filling in all the border
        indexes of the _layout list with rectangles"""
        for i in range(1000 // self.size):
            self.draw(i, 0)
            self.draw(i, 500 // self.size - 1)

        for i in range(1, 500 // self.size - 1):
            self.draw(0, i)
            self.draw(1000 // self.size - 1, i)

    def map1(self):
        """Draws layout 1 by filling in specific indexes of the
        _layout list with rectangles. Automatically mirrors
        the layout horizontally"""
        coord = [
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
        ]

        for loc in coord:
            self.draw(loc[0], loc[1])
            self.draw(1000 // self.size - 1 - loc[0], loc[1])
