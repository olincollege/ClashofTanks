"""Unit tests for MVC related functions that are testable

This means that we're not testing the view portion
of our code since it's just drawing things based on
information from model class.

Furthermore, functions without parameters are not 
tested since there is no changing variable that we
can use. Internal helper functions used for abstraction
will also not be unit tested since it runs other
functions that are already unit tested. """
# pylint: disable-all
import pytest
import pygame
from game_controller import GameController
from game_model import GameModel
from game_view import GameView

pygame.init()
pygame.mixer.init()


INPUTS = [
    # Input with corresponding action Rotate
    (pygame.K_a, [22.5, 150, 250]),
    # Input with corresponding action Move
    (pygame.K_w, [0, 160, 250]),
    # Input without corresponding action
    (pygame.K_g, [0, 150, 250]),
    # Not even an valid pygame Event input
    ("pygame.K_g", [0, 150, 250]),
    # Not even an valid pygame Event input
    (42, [0, 150, 250]),
]

START = [
    # Input with corresponding action Rotate
    (True, True),
    # Input is False
    (False, False),
    # Input isn't valid (str)
    ("WHE", True),
    # Input isn't valid (int)
    (42, True),
]


# Controller Function Unit Tests
@pytest.mark.parametrize("event, key", INPUTS)
def test_inputs(event, key):
    """We test whether the function can handle
    edge cases for inputs not found in the dictionary
    or of the wrong type, and whether it can run the functions that
    it can handle.

    We'll just be testing that

    Args:
        event: A Pygame Event
        key: An list. The first index is a int or a float for the angle,
        second index is x location, and 3rd index is y location
        which is the correct values after the event inputs.
    """
    model = GameModel()
    controller = GameController(model)
    controller.get_inputs(event)

    assert [
        model.player1.angle,
        model.player1.tank_x,
        model.player1.tank_y,
    ] == key


# Model Unit Tests
@pytest.mark.parametrize("boolean, key", START)
def test_shooting(boolean, key):
    """We test whether the function can handle
    edge cases for the start function in the model


    Args:
        boolean: An ideally boolean value but
        can be a string or int for edge cases
        key: A boolean value for both gameover and splash
        attributes
    """
    model = GameModel()

    model.start(boolean)

    assert model.splash == key
    assert model.gameover == key
