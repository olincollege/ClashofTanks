""""Controller Class of the MVC game Combat"""
import pygame


class GameController:

    """Receives and handles user controller inputs"""

    def __init__(self, model):
        """Initialization Function
        Args:
            model: A GameModel Object
        """

        # _model is a GameModel Object
        self._model = model
        # _move is an int that controls the tank movement input
        self._move = 5
        # _turn is a float that controls the angle a tank rotates by
        self._turn = 22.5

        # _input_types is a dictionary with the keys being
        # different player input keys and the values being
        # different functions
        self._input_types = {
            # Player 1 Keys
            pygame.K_a: lambda: self._model.player1.rotate(self._turn),
            pygame.K_w: lambda: self._model.player1.move(self._move),
            pygame.K_s: lambda: self._model.player1.move(-self._move),
            pygame.K_d: lambda: self._model.player1.rotate(-self._turn),
            pygame.K_e: lambda: self._model.bullet1.moving(
                True,
                (self._model.player1.tank_x, self._model.player1.tank_y),
                self._model.player1.angle,
            ),
            # Player 2 Keys
            pygame.K_j: lambda: self._model.player2.rotate(self._turn),
            pygame.K_i: lambda: self._model.player2.move(self._move),
            pygame.K_k: lambda: self._model.player2.move(-self._move),
            pygame.K_l: lambda: self._model.player2.rotate(-self._turn),
            pygame.K_o: lambda: self._model.bullet2.moving(
                True,
                (self._model.player2.tank_x, self._model.player2.tank_y),
                self._model.player2.angle,
            ),
            # Other keyboard inputs
            pygame.K_SPACE: self._model.restart,
            pygame.K_RETURN: lambda: self._model.start(False),
        }

    def get_inputs(self, inputs):
        """A function that takes all user
        inputs per frame

        Args:
            inputs: A pygame Event object
        """
        if inputs in self._input_types:
            self._input_types[inputs]()

    def __repr__(self):
        """Displays information of the class in a string
        format.
        Return:
            A string with the list of input types available"""
        return f"{self._input_types}"
