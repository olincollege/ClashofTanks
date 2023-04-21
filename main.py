"""Main file with super loop"""

import pygame

pygame.init()


# WIP Only to demonstrate how the super loop works. ALl this will be abstracted into a class later.
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Atari 2600 Tank")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


# Display some text
font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10, 10, 10))

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()


# Our main function which houses the super loop
def main():
    ##Super loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
