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
        tank2 = model.player2
        # !!!The order of blits matter!!!

        tank1_img = pygame.image.load("Tank1.png").convert_alpha()
        tank2_img = pygame.image.load("Tank1.png").convert_alpha()

        # Drawing the background
        self._screen.blit(self._background, (0, 0))

        # Drawing Tank1
        img1 = pygame.transform.rotate(tank1_img, tank1.angle)
        self._screen.blit(
            img1,
            (
                tank1.x - int(img1.get_width() / 2),
                tank1.y - int(img1.get_height() / 2),
            ),
        )

        # Drawing Tank2
        img2 = pygame.transform.rotate(tank2_img, tank2.angle)
        self._screen.blit(
            img2,
            (
                tank2.x - int(img2.get_width() / 2),
                tank2.y - int(img2.get_height() / 2),
            ),
        )
        # Only for debugging purposes, shows hitbox

        if model.bullet1._moving == True:
            pygame.draw.rect(self._screen, (100, 0, 200), model.bullet1.bullet)

        if model.bullet2._moving == True:
            pygame.draw.rect(self._screen, (100, 0, 200), model.bullet2.bullet)
        pygame.draw.rect(self._screen, (255, 0, 0), tank1.hitbox)
        pygame.draw.rect(self._screen, (255, 255, 0), tank2.hitbox)

        pygame.display.flip()
