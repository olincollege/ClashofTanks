"""Main file with super loop"""

import pygame

from GameView import GameView
from GameModel import GameModel
from GameController import GameController


class Game:
    def __init__(self):
        # Initializes MVC
        pygame.init()
        self.model = GameModel()
        self.controller = GameController(self.model)
        self.view = GameView()

    # Super/Game loop
    def main(self):
        while True:
            for event in pygame.event.get():
                # If input was made
                if event.type == pygame.KEYDOWN:
                    self.controller.inputs(event.key)
                # If user wants to quit
                if event.type == pygame.QUIT:
                    return

            self.model.update()
            self.view.update(self.model)


if __name__ == "__main__":
    game = Game()
    game.main()
