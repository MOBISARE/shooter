import random

import pygame
from pygame.sprite import Sprite

import constants


class Comet(Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load(constants.COMET_PATH)
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(constants.LEFT_EDGE, constants.RIGHT_EDGE)
        self.rect.y = - random.randint(0, constants.SCREEN_HEIGHT)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monsters()
            self.comet_event.game.spawn_monsters()
            self.comet_event.game.spawn_monsters()


    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= constants.GROUND:
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collisison(self, self.comet_event.game.group_players):
            self.remove()
            self.comet_event.game.player.damage(20)

