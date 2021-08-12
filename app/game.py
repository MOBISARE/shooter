import os

import pygame.display
from pygame.time import Clock

import constants
from monster import Monster
from player import Player
from pygame.sprite import Group, Sprite


class Game:

    # Constructor
    def __init__(self) -> None:

        # making the screen

        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Shooter")

        # making the background
        self.background = pygame.image.load(constants.BACKGROUND_PATH)

        # load the player
        self.group_players = Group()
        self.player = Player(self)
        self.group_players.add(self.player)
        self.pressed = {}


        # group of monsters
        self.group_monsters = Group()
        self.spawn_monsters()
        self.spawn_monsters()

    # Main loop of the game
    def run(self) -> None:

        clock = Clock()
        running = True
        while running:

            # apply background
            self.screen.blit(self.background, (0, -200))

            # apply the player
            self.screen.blit(self.player.image, self.player.rect)

            # update player's health bar
            self.player.update_health_bar(self.screen)

            for projectile in self.player.all_projectiles:
                projectile.move()

            for monster in self.group_monsters:
                monster.forward()
                monster.update_health_bar(self.screen)

            # apply the projectiles
            self.player.all_projectiles.draw(self.screen)

            # apply monsters
            self.group_monsters.draw(self.screen)

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

    def spawn_monsters(self) -> None:
        monster = Monster(self)
        self.group_monsters.add(monster)

    def check_collisison(self, sprite: Sprite, group: Group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)