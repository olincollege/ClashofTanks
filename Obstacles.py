"""Obstacles """

import pygame


class Obstacles:
    def __init__(self, map):
        self.size = 25
        self.frame = 0

        self._layout = [
            [0 for i in range(1000 // self.size)]
            for i in range(500 // self.size)
        ]
        self.border()
        if map == 1:
            self.map1()

    @property
    def layout(self):
        return self._layout

    def draw(self, x, y):
        self._layout[y][x] = pygame.Rect(
            x * self.size, y * self.size, self.size, self.size
        )

    def border(self):
        for i in range(1000 // self.size):
            self.draw(i, 0)
            self.draw(i, 500 // self.size - 1)

        for i in range(1, 500 // self.size - 1):
            self.draw(0, i)
            self.draw(1000 // self.size - 1, i)

    def map1(self):
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
