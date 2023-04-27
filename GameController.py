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
            # Player 2 Keys
            pygame.K_j: lambda: self._model.player2.rotate(self._turn),
            pygame.K_i: lambda: self._model.player2.move(self._move),
            pygame.K_k: lambda: self._model.player2.move(-self._move),
            pygame.K_l: lambda: self._model.player2.rotate(-self._turn),
        }

    def inputs(self, input):
        if input in self._input_types:
            self._input_types[input]()
