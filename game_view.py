""""View Class of the MVC game Combat"""

import pygame


class GameView:
    """GameView Class visualizes the overall game

    Attributes:
        timing: An int value that keeps track of
        the frames while the game runs
    """

    def __init__(self):
        """
        Initializes the GameView class and sets the window
        and background
        """
        # Initalizing the window screen
        pygame.font.get_init()
        self._screen = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption("Atari 2600 Tank")
        self._background = pygame.Surface(self._screen.get_size()).convert()
        self._background.fill((0, 0, 0))
        self.timing = pygame.time.get_ticks()
        self.scoreboard = ""

    def update(self, model):
        """Update function that updates the screen for each frame
        Args:
            model: A GameModel object that contains all
            information regarding the model of the game"""

        # saving which player is which
        tank1 = model.player1
        tank2 = model.player2

        # Loading the png files for the tanks
        tank1_img = pygame.image.load("Tank1.png").convert_alpha()
        tank2_img = pygame.image.load("Tank1.png").convert_alpha()

        # Drawing the background
        self._background.fill((153, 0, 0))
        self._screen.blit(self._background, (0, 0))

        # Drawing Scoreboard

        font1 = pygame.font.SysFont("freesanbold.ttf", 50)
        win_score = 10
        # Check winner
        if model.scores[0] == win_score:
            self.scoreboard = "P1 wins"
        elif model.scores[1] == win_score:
            self.scoreboard = "P2 Wins"
        # Scoreboard update
        else:
            self.scoreboard = f"{model.scores[0]} : {model.scores[1]}"
        scoreboard = font1.render(self.scoreboard, False, (230, 191, 0))
        self._screen.blit(scoreboard, (465, 60))

        # Drawing Tank1
        img1 = pygame.transform.rotate(tank1_img, tank1.angle)
        self._screen.blit(
            img1,
            (
                tank1.tank_x - int(img1.get_width() / 2),
                tank1.tank_y - int(img1.get_height() / 2),
            ),
        )

        # Drawing Tank2
        img2 = pygame.transform.rotate(tank2_img, tank2.angle)
        self._screen.blit(
            img2,
            (
                tank2.tank_x - int(img2.get_width() / 2),
                tank2.tank_y - int(img2.get_height() / 2),
            ),
        )

        # Draw Bullets
        if model.bullet1.is_moving is True:
            pygame.draw.rect(self._screen, (0, 0, 0), model.bullet1.bullet)

        if model.bullet2.is_moving is True:
            pygame.draw.rect(self._screen, (0, 0, 200), model.bullet2.bullet)

        # Drawing Obstacles
        for row in model.map.layout:
            for column in row:
                if column != 0:
                    pygame.draw.rect(self._screen, (230, 191, 0), column)

        pygame.display.flip()

    def splashpage(self):
        """A function that draws a splash page
        on the screen
        """

        self.timing += 1
        # Drawing the background
        self._screen.blit(self._background, (0, 0))
        font1 = pygame.font.SysFont("freesanbold.ttf", 100)
        font2 = pygame.font.SysFont("notomono.ttf", 50)
        font3 = pygame.font.SysFont("notomono.ttf", 40)

        title = font1.render("--COMBAT--", False, (77, 106, 255))
        authors = font3.render(
            "By: Allan Huang, Sidney Taylor, Trinity Lee",
            False,
            (153, 170, 255),
        )

        press_s = font2.render("Press SPACE to start", False, (255, 255, 255))
        self._screen.blit(title, (300, 60))
        self._screen.blit(authors, (200, 150))

        # Creates a blinking affect for the press_s text
        if abs(self.timing - pygame.time.get_ticks()) > 200:
            self._screen.blit(press_s, (330, 300))

        if abs(self.timing - pygame.time.get_ticks()) >= 400:
            self.timing = pygame.time.get_ticks()

        pygame.display.flip()

    def gameover(
        self,
    ):
        """A function that draws the game
        over screen

        Args:
            model: A GameModel object used to
            draw the game over the screen.
        """

        self._screen.blit(self._background, (0, 0))
        font2 = pygame.font.SysFont("notomono.ttf", 50)

        # Draws who the winner is
        winner = font2.render(self.scoreboard, False, (77, 106, 255))
        again = font2.render("press SPACE to restart", False, (255, 255, 255))
        self._screen.blit(winner, (400, 60))
        self._screen.blit(again, (330, 150))
        pygame.display.flip()
