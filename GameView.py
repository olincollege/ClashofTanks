"""View"""

"""Visualizes the overall game"""
import pygame


class GameView:
    def __init__(self):
        """
        Initializes the GameView class and sets the window
        and background

        Attributes:
            self._screen: A Surface object that determines
            the overall screen window size with the inputs
            self._background: A surface object hat controls
            how the background looks
            self._color:A tuple that controls RGB background color

        """
        # Initalizing the window screen
        self._screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Atari 2600 Tank")
        self._background = pygame.Surface(self._screen.get_size()).convert()
        self._color = (250, 250, 250)
        self._background.fill(self._color)

    def update(self, model):
        """Update function for GameView
        Args:
            model: A GameModel object
            that contains all information regarding to
            the model of the game"""

        # tank1 is a
        tank1 = model.player1
        # !!!The order of blits matter!!!

        tank1_img = pygame.image.load("Tank1.png").convert_alpha()

        # Drawing the background
        self._screen.blit(self._background, (0, 0))

        # Drawing the image
        self._screen.blit(tank1_img, (tank1.x, tank1.y))

        # Only for debugging purposes, shows hitbox
        pygame.draw.rect(self._screen, (255, 0, 0), tank1.hitbox)

        pygame.display.flip()
