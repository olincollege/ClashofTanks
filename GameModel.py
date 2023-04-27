""""Model"""

import pygame

from Tank import Tank
from Bullet import Bullet


class GameModel:
    def __init__(self):
        """Initializes GameModel object and attributes
        Attributes:
            SPEED: An int that determines tank speed movement
            HEALTH: An int that determines total tank health

            player1: A Tank object for Player 1
            bullet1: A Bullet object for Player 1"""
        # Initalizing Groups
        self._p1 = pygame.sprite.Group()
        self._p2 = pygame.sprite.Group()

        # Constants
        self.SPEED = 2
        self.HEALTH = 2

        # Making Player 1 Tank & Bullet. Same sprite Group
        self.player1 = Tank((200, 100), self._p1, self.HEALTH, self.SPEED)
        self.bullet1 = Bullet(
            self._p1, self.player1.x, self.player1.y, self.player1.angle
        )

        # Making Player 2 Tank & Bullet. Same sprite Group
        self.player2 = Tank((400, 100), self._p2, self.HEALTH, self.SPEED)
        self.bullet2 = Bullet(
            self._p2, self.player2.x, self.player2.y, self.player2.angle
        )
