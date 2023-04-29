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
        self.score1 = 0
        self.score2 = 0

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

    def update(self):
        self.shooting(self.bullet1, self.player1)
        self.shooting(self.bullet2, self.player2)

        if pygame.Rect.colliderect(self.bullet1.bullet, self.player2.hitbox):
            self.bullet1.moving(
                False, self.player1.x, self.player1.y, self.player1.angle
            )
            self.score1 += 1

        if pygame.Rect.colliderect(self.bullet2.bullet, self.player1.hitbox):
            self.bullet2.moving(
                False, self.player2.x, self.player2.y, self.player2.angle
            )
            self.score2 += 1

        # Check winner
        if self.score1 == 10:
            print("P1 wins")
            self.score1 = 0
        if self.score2 == 10:
            print("P2 Wins")
            self.score2 = 0

    # Helper Functions
    def shooting(self, bullet, player):
        if bullet._moving == True:
            # Moves for
            if abs(bullet.time - pygame.time.get_ticks()) > 1000:
                bullet.moving(False, player.x, player.y, player.angle)
            else:
                bullet.move()
