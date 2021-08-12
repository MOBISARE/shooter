import os

import pygame.display
from pygame.time import Clock

import constants
from player import Player


class Game:

    # Constructor
    def __init__(self) -> None:

        # making the screen

        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Shooter")

        # making the background
        self.background = pygame.image.load(constants.BACKGROUND_PATH)

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

            for projectile in self.player.all_projectiles:
                projectile.move()

            # apply the projectiles
            self.player.all_projectiles.draw(self.screen)

            # key pressed verification
            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < constants.RIGHT_EDGE:
                self.player.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > constants.LEFT_EDGE:
                self.player.move_left()

            # update
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                    if event.key == pygame.K_SPACE:
                        self.player.launch_projectile()

                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False

            clock.tick(constants.FRAME)
        print("Exiting...")
        pygame.quit()
