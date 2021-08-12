import os

import pygame
from pygame.sprite import Sprite

import constants


class Projectile(Sprite):

    # Constructor
    def __init__(self, player) -> None:
        super().__init__()

        # Constants
        self.player = player
        self.velocity = constants.PROJECTILE_VELOCITY
        self.image = pygame.image.load(constants.PROJECTILE_PATH)
        self.image = pygame.transform.scale(self.image, (constants.PROJECTILE_SIZE, constants.PROJECTILE_SIZE))
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + constants.PROJECTILE_SCALE_X
        self.rect.y = player.rect.y + constants.PROJECTILE_SCALE_Y
        self.angle = 0

    def move(self) -> None:
        self.rect.x += self.velocity
        self.rotate()

        if self.rect.x > constants.RIGHT_OUT:
            self.remove()

        if self.player.game.check_collisison(self, self.player.game.group_monsters):
            self.remove()

    def remove(self) -> None:
        self.player.all_projectiles.remove(self)

    def rotate(self):
        self.angle -= constants.PROJECTILE_ROTATION
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


