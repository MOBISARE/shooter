import random
import pygame
import constants
from animation import AnimateSprite
from typing import Tuple


class Monster(AnimateSprite):

    def __init__(self, game, name: str, size: Tuple[int, int], offset: int =constants.DEFAULT_OFFSET) -> None:
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.loot_amount = 10

    def forward(self) -> None:
        if not self.game.check_collisison(self, self.game.group_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def update_animation(self):
        self.animate(loop=True)

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
            self.velocity = random.randint(1, self.default_speed)
            self.game.add_score(self.loot_amount)

            if self.game.comet_event.is_full_loaded():
                self.game.group_monsters.remove(self)
                self.game.comet_event.attempt_fall()
