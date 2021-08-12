import pygame
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface

import constants


class Monster(Sprite):

    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health: int = 100
        self.max_health: int = 100
        self.attack: int = 5
        self.velocity: int = 5
        self.image: Surface = pygame.image.load(constants.MONSTER_PATH)
        self.rect: Rect = self.image.get_rect()

        self.rect.x = 1000
        self.rect.y = 540

    def forward(self) -> None:
        if not self.game.check_collisison(self, self.game.group_players):
            self.rect.x -= self.velocity
