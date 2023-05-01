"""Controller"""

import pygame


class GameController:

    """Receives and handles controller inputs

    Attributes:
        _model: A GameModel object
            that contains all information regarding to
            the model of the game"""

    def __init__(self, model):
        """Initialization Function"""
        self._model = model
        self._move = 5
        self._turn = 22.5

        self._input_types = {
            # Player 1 Keys
            pygame.K_a: lambda: self._model.player1.rotate(self._turn),
            pygame.K_w: lambda: self._model.player1.move(self._move),
            pygame.K_s: lambda: self._model.player1.move(-self._move),
            pygame.K_d: lambda: self._model.player1.rotate(-self._turn),
            pygame.K_e: lambda: self._model.bullet1.moving(
                True,
                self._model.player1.x,
                self._model.player1.y,
                self._model.player1.angle,
            ),
            # Player 2 Keys
            pygame.K_j: lambda: self._model.player2.rotate(self._turn),
            pygame.K_i: lambda: self._model.player2.move(self._move),
            pygame.K_k: lambda: self._model.player2.move(-self._move),
            pygame.K_l: lambda: self._model.player2.rotate(-self._turn),
            pygame.K_o: lambda: self._model.bullet2.moving(
                True,
                self._model.player2.x,
                self._model.player2.y,
                self._model.player2.angle,
            ),
            # Other keyboard inputs
            pygame.K_SPACE: lambda: self._model.restart(),
            pygame.K_s: lambda: self._model.start(False),
        }

    def inputs(self, input):
        if input in self._input_types:
            self._input_types[input]()
