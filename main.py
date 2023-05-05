"""Main file with super loop"""

import pygame

from game_view import GameView
from game_model import GameModel
from game_controller import GameController


class Game:

    """A class that runs the entire Atari 2600 Combat
    game

    Attributes:
        model: A GameModel object
        controller: A GameController object
        view: A GameView object
    """

    def __init__(self):
        # Initializes MVC
        """Initializes the Game class"""
        pygame.init()
        pygame.mixer.init()
        self.model = GameModel()
        self.controller = GameController(self.model)
        self.view = GameView()

    # Super/Game loop
    def main(self):
        """The main function which runs the game loop &
        handles different screen displays and input events
        """

        # Game Loop
        while True:
            for event in pygame.event.get():
                # If input was made
                if event.type == pygame.KEYDOWN:
                    self.controller.get_inputs(event.key)
                # If user wants to quit
                if event.type == pygame.QUIT:
                    return

            if self.model.splash and self.model.gameover:
                self.view.splashpage()
            elif self.model.gameover:
                self.view.gameover()

            else:
                self.model.update()
                self.view.update(self.model)

    def __repr__(self):
        """A string representation of the class.
        Return:
            Information on the model, view, and controller
            classes used in the game
        """
        return f"{self.model}, {self.view}, {self.controller}"


if __name__ == "__main__":
    game = Game()
    game.main()
