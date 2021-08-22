import pygame.sprite

import constants
from projectile import Projectile
from pygame.sprite import Sprite
from animation import AnimateSprite


class Player(AnimateSprite):

    def __init__(self, game) -> None:
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = constants.GROUND

    def move_right(self) -> None:
        if not self.game.check_collisison(self, self.game.group_monsters):
            self.rect.x += self.velocity

    def move_left(self) -> None:
        self.rect.x -= self.velocity

    def launch_projectile(self) -> None:
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        self.start_animation()
        self.game.sound_manager.play("tir")

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface) -> None:
        bar_color = (50, 255, 26)
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
        back_bar_color = (87, 87, 87)
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()