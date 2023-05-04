""""Model Class of the MVC game Combat"""
from random import randrange
import pygame
from tank import Tank
from bullet import Bullet
from obstacles import Obstacles


class GameModel:
    """The Model Class for the Atari 2600 Combat game

    Attributes:
            scores: a list with 2 int that keeps track of Player 1 & 2's score
            map: a Obstacles object which set the obstacle layout
            of the game

            player1: A Tank object for Player 1
            bullet1: A Bullet object for Player 1
            player2: A Tank object for Player 2
            bullet2: A Bullet object for Player 2"""

    def __init__(self):
        """Initializes GameModel object and external and
        internal attributes"""
        # Initalizing Groups

        self.scores = [0, 0]

        self.map = Obstacles(2)
        self.states = {"gameover": True, "splash": True}

        # Making Player 1 Tank & Bullet. Same sprite Group
        self.player1 = Tank((150, 250), pygame.sprite.Group(), 2)
        self.bullet1 = Bullet(
            pygame.sprite.Group(),
            (self.player1.tank_x, self.player1.tank_y),
            self.player1.angle,
        )

        # Making Player 2 Tank & Bullet. Same sprite Group
        self.player2 = Tank((850, 250), pygame.sprite.Group(), 2, 180)
        self.bullet2 = Bullet(
            pygame.sprite.Group(),
            (self.player2.tank_x, self.player2.tank_y),
            self.player2.angle,
        )

    def update(self):
        """A update function which keeps track of the game's state and
        manages the behavior of all the objects

        It controls the shooting of the bullets, the collision detection, and
        whether the game is over or not."""

        # Using Helper Function for shooting bullet behavior
        self.shooting(self.bullet1, self.player1)
        self.shooting(self.bullet2, self.player2)

        # Collision Detection
        # player 1's bullet hitting player2
        if pygame.Rect.colliderect(self.bullet1.bullet, self.player2.hitbox):
            self.bullet1.moving(
                False,
                (self.player1.tank_x, self.player1.tank_y),
                self.player1.angle,
            )
            # Update score & start next round
            self.scores[0] += 1
            pygame.mixer.Sound.play(pygame.mixer.Sound("audio/explosion.mp3"))
            pygame.mixer.music.stop()
            self.next_round()

        # Player 2's bullet hitting player 1
        if pygame.Rect.colliderect(self.bullet2.bullet, self.player1.hitbox):
            self.bullet2.moving(
                False,
                (self.player2.tank_x, self.player2.tank_y),
                self.player2.angle,
            )
            # Update score & start next round
            self.scores[1] += 1

            pygame.mixer.Sound.play(pygame.mixer.Sound("audio/explosion.mp3"))
            pygame.mixer.music.stop()
            self.next_round()

        # Obstacle Collision Detection
        for row in self.map.layout:
            for obstacle in row:
                if obstacle != 0:
                    # Bullet1 interaction with an obstacle
                    if pygame.Rect.colliderect(self.bullet1.bullet, obstacle):
                        self.bullet1.ricochet()
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound("audio/ricochet.wav")
                        )
                        pygame.mixer.music.stop()

                    # Bullet2 interaction with an obstacle
                    if pygame.Rect.colliderect(self.bullet2.bullet, obstacle):
                        self.bullet2.ricochet()
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound("audio/ricochet.wav")
                        )
                        pygame.mixer.music.stop()

                    # Tanks don't go through obstacles
                    if pygame.Rect.colliderect(self.player1.hitbox, obstacle):
                        self.player1.move(self.player1.lastdir * -1)
                    if pygame.Rect.colliderect(self.player2.hitbox, obstacle):
                        self.player2.move(self.player2.lastdir * -1)

        # win_score is the number of points a player needs to win
        win_score = 10
        # Check winner
        if win_score in (self.scores[0], self.scores[1]):
            self.states["gameover"] = True
            self.states["splash"] = False

    # Helper Functions
    def next_round(self):
        """
        A helper function which resets the position of
        the tanks and the bullet for when the next round starts
        """
        # Resetting Player 1 Tank & Bullet. Same sprite Group
        self.player1 = Tank((150, 250), pygame.sprite.Group(), 2)
        self.bullet1 = Bullet(
            pygame.sprite.Group(),
            (self.player1.tank_x, self.player1.tank_y),
            self.player1.angle,
        )

        # Resetting Player 2 Tank & Bullet. Same sprite Group
        self.player2 = Tank((850, 250), pygame.sprite.Group(), 2, 180)
        self.bullet2 = Bullet(
            pygame.sprite.Group(),
            (self.player2.tank_x, self.player2.tank_y),
            self.player2.angle,
        )

    def restart(self):
        """
        A helper function that resets the entire state of the model by resetting
        all the mutable variables that were used throughout the game.
        """
        pygame.mixer.Sound.play(pygame.mixer.Sound("audio/restart.wav"))
        pygame.mixer.music.stop()

        # Checks that the game is over
        if self.states["gameover"]:
            self.scores = [0, 0]
            self.map = Obstacles(randrange(0, 5))
            self.states["gameover"] = False

            # restarting all the tank objects
            self.restart()

    def shooting(self, bullet, player):
        """A helper function that identifies whether a bullet is moving
        and then updates it's movement. If a bullet is supposed to be moving,
        it will move for 3000 frames.

        Args:
            bullet: A Bullet object
            player: A Tank object"""

        # If a bullet is supposed to be moving
        if bullet.is_moving is True:
            # Moves for 3000 frames
            if abs(bullet.time - pygame.time.get_ticks()) > 3000:
                # Stop moving
                bullet.moving(
                    False, (player.tank_x, player.tank_y), player.angle
                )
            else:
                bullet.move()

    def start(self, value):
        """A function that sets the value of the gameover and
         splash values

        Args:
            value: A boolean value used to determine what
            the values of the attributes will be."""
        self.states["gameover"] = value
        self.states["splash"] = value

    # properties
    @property
    def gameover(self):
        """A decorator function for the the internal gameover attribute

        Return:
            the boolean _gameover value"""
        return self.states["gameover"]

    @property
    def splash(self):
        """A decorator function for the the internal splash attribute

        Return:
            the boolean _splash value"""
        return self.states["splash"]

    def __repr__(self):
        """Displays critical information of the state of the game.

        Return:
            A string with information on the current scoreboard
            and gameover state."""
        return f"{self.gameover}"
