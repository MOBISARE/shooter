import random

import pygame
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface

import constants
from animation import AnimateSprite


class Monster(AnimateSprite):

    def __init__(self, game) -> None:
        super().__init__("mummy")
        self.game = game
        self.health: int = 100
        self.max_health: int = 100
        self.attack: float = 0.3
        self.velocity: int = random.randint(1, 3)
        #self.image: Surface = pygame.image.load(constants.MONSTER_PATH)
        self.rect: Rect = self.image.get_rect()

        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def forward(self) -> None:
        if not self.game.check_collisison(self, self.game.group_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


    def update_animation(self):
        self.animate()


    def update_health_bar(self, surface) -> None:
        bar_color = (50, 255, 26)
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        back_bar_color = (87, 87, 87)
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount) -> None:
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1080
            self.health = self.max_health
            self.velocity = random.randint(1, 3)

            if self.game.comet_event.is_full_loaded():
                self.game.group_monsters.remove(self)
                self.game.comet_event.attempt_fall()
