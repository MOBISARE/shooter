import os

import pygame.display
from pygame.time import Clock


class Game:

    # Constructor
    def __init__(self) -> None:

        # making the screen
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Shooter")

        # making the background
        print(os.path.exists("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/bg.jpg"))
        self.background = pygame.image.load("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/bg.jpg")


    # Main loop of the game
    def run(self) -> None:

        clock = Clock()
        running = True
        while running:

            # apply background
            self.screen.blit(self.background, (0, 0))


            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        print("Exiting...")
        pygame.quit()
