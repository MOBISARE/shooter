import os

import pygame.display
from pygame.time import Clock

from player import Player


class Game:



    # Constructor
    def __init__(self) -> None:

        # Constants
        self.WIDTH = 1080
        self.HEIGHT = 720
        self.LEFT_EDGE = -40
        self.RIGHT_EDGE = 920
        # making the screen

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Shooter")

        # making the background
        print(os.path.exists("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/bg.jpg"))
        self.background = pygame.image.load("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/bg.jpg")

        # load the player
        self.player = Player()

        self.pressed = {}



    # Main loop of the game
    def run(self) -> None:

        clock = Clock()
        running = True
        while running:

            # apply background
            self.screen.blit(self.background, (0, -200))

            # apply the player
            self.screen.blit(self.player.image, self.player.rect)

            # key pressed verification
            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < self.RIGHT_EDGE:
                self.player.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > self.LEFT_EDGE:
                self.player.move_left()


            # update
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False

            clock.tick(60)
        print("Exiting...")
        pygame.quit()
