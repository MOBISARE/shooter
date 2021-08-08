import os

import pygame.display
from pygame.time import Clock

from player import Player


class Game:

    # Constructor
    def __init__(self) -> None:

        # making the screen
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Shooter")

        # making the background
        print(os.path.exists("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/bg.jpg"))
        self.background = pygame.image.load("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/bg.jpg")

        # load the player
        self.player = Player()



    # Main loop of the game
    def run(self) -> None:

        clock = Clock()
        running = True
        while running:

            # apply background
            self.screen.blit(self.background, (0, -200))

            # apply the player
            self.screen.blit(self.player.image, self.player.rect)

            # update
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        print("Exiting...")
        pygame.quit()
