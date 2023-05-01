""""Model"""

import pygame
from Tank import Tank
from Bullet import Bullet
from Obstacles import Obstacles


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
        self.map = Obstacles(1)
        self.scoreboard = f"{self.score1} : {self.score2}"
        self._gameover = True
        self._splash = True

        # Constants
        self.SPEED = 2
        self.HEALTH = 2

        # Making Player 1 Tank & Bullet. Same sprite Group
        self.player1 = Tank((150, 250), self._p1, self.HEALTH, self.SPEED)
        self.bullet1 = Bullet(
            self._p1, self.player1.x, self.player1.y, self.player1.angle
        )

        # Making Player 2 Tank & Bullet. Same sprite Group
        self.player2 = Tank((850, 250), self._p2, self.HEALTH, self.SPEED, 180)
        self.bullet2 = Bullet(
            self._p2, self.player2.x, self.player2.y, self.player2.angle
        )

    def update(self):
        # Using Helper Function for shooting behavior
        self.shooting(self.bullet1, self.player1)
        self.shooting(self.bullet2, self.player2)

        # player 1's bullet hitting player2
        if pygame.Rect.colliderect(self.bullet1.bullet, self.player2.hitbox):
            self.bullet1.moving(
                False, self.player1.x, self.player1.y, self.player1.angle
            )
            self.score1 += 1
            self.next_round()

        # Player 2's bullet hitting player 1
        if pygame.Rect.colliderect(self.bullet2.bullet, self.player1.hitbox):
            self.bullet2.moving(
                False, self.player2.x, self.player2.y, self.player2.angle
            )
            self.score2 += 1
            self.next_round()

        # Obstacle Collision Detection
        for row in self.map.layout:
            for obstacle in row:
                if obstacle != 0:
                    # Bullet1 interaction with an obstacle
                    if pygame.Rect.colliderect(self.bullet1.bullet, obstacle):
                        self.bullet1.ricochet()

                    # Bullet2 interaction with an obstacle
                    if pygame.Rect.colliderect(self.bullet2.bullet, obstacle):
                        self.bullet2.ricochet()

                    if pygame.Rect.colliderect(self.player1.hitbox, obstacle):
                        self.player1.move(self.player1.lastdir * -1)
                    if pygame.Rect.colliderect(self.player2.hitbox, obstacle):
                        self.player2.move(self.player2.lastdir * -1)

        win_score = 10
        # Check winner
        if self.score1 == win_score:
            self.scoreboard = "P1 wins"
            self._gameover = True
        elif self.score2 == win_score:
            self.scoreboard = "P2 Wins"
            self._gameover = True

        # Scoreboard update
        else:
            self.scoreboard = f"{self.score1} : {self.score2}"

    def next_round(self):
        # Making Player 1 Tank & Bullet. Same sprite Group
        self.player1 = Tank((150, 250), self._p1, self.HEALTH, self.SPEED)
        self.bullet1 = Bullet(
            self._p1, self.player1.x, self.player1.y, self.player1.angle
        )

        # Making Player 2 Tank & Bullet. Same sprite Group
        self.player2 = Tank((850, 250), self._p2, self.HEALTH, self.SPEED, 180)
        self.bullet2 = Bullet(
            self._p2, self.player2.x, self.player2.y, self.player2.angle
        )

    def restart(self):
        if not self._gameover:
            return
        self.score1 = 0
        self.score2 = 0
        self.map = Obstacles(1)
        self.scoreboard = f"{self.score1} : {self.score2}"
        self._gameover = False

        # Making Player 1 Tank & Bullet. Same sprite Group
        self.player1 = Tank((150, 250), self._p1, self.HEALTH, self.SPEED)
        self.bullet1 = Bullet(
            self._p1, self.player1.x, self.player1.y, self.player1.angle
        )

        # Making Player 2 Tank & Bullet. Same sprite Group
        self.player2 = Tank((850, 250), self._p2, self.HEALTH, self.SPEED, 180)
        self.bullet2 = Bullet(
            self._p2, self.player2.x, self.player2.y, self.player2.angle
        )

    @property
    def gameover(self):
        return self._gameover

    @property
    def splash(self):
        return self._splash

    @splash.setter
    def ended(self, value):
        self._splash = value

    def start(self, value):
        self._gameover = value
        self._splash = value

    # Helper Functions
    def shooting(self, bullet, player):
        if bullet._moving == True:
            # Moves for
            if abs(bullet.time - pygame.time.get_ticks()) > 3000:
                bullet.moving(False, player.x, player.y, player.angle)
            else:
                bullet.move()
