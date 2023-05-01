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
        pygame.font.get_init()

        self._screen = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption("Atari 2600 Tank")
        self._background = pygame.Surface(self._screen.get_size()).convert()
        self._color = (153, 0, 0)
        self._background.fill(self._color)

    def update(self, model):
        """Update function for GameView
        Args:
            model: A GameModel object
            that contains all information regarding to
            the model of the game"""

        # saving which player is which
        tank1 = model.player1
        tank2 = model.player2

        # Loading the png files for the tanks
        tank1_img = pygame.image.load("Tank1.png").convert_alpha()
        tank2_img = pygame.image.load("Tank1.png").convert_alpha()

        # Drawing the background
        self._screen.blit(self._background, (0, 0))

        # Drawing Scoreboard
        font1 = pygame.font.SysFont("freesanbold.ttf", 50)
        scoreboard = font1.render(model.scoreboard, False, (230, 191, 0))
        self._screen.blit(scoreboard, (465, 60))

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

        # Draw Bullets
        if model.bullet1._moving == True:
            pygame.draw.rect(self._screen, (0, 0, 0), model.bullet1.bullet)

        if model.bullet2._moving == True:
            pygame.draw.rect(self._screen, (0, 0, 200), model.bullet2.bullet)

        # Drawing Obstacles
        for row in model.map.layout:
            for column in row:
                if column != 0:
                    pygame.draw.rect(self._screen, (230, 191, 0), column)

        pygame.display.flip()

    def splashpage(self):
        # Drawing the background
        self._screen.blit(self._background, (0, 0))
        font1 = pygame.font.SysFont("freesanbold.ttf", 50)
        scoreboard = font1.render("COMBAT", False, (230, 191, 0))
        self._screen.blit(scoreboard, (465, 60))
