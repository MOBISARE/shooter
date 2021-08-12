import pygame.sprite

import constants
from projectile import Projectile
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load(constants.PLAYER_PATH)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self) -> None:
        self.rect.x += self.velocity

    def move_left(self) -> None:
        self.rect.x -= self.velocity

    def launch_projectile(self) -> None:
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
