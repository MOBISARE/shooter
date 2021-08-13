import pygame
from pygame._sprite import Group

from comet import Comet


class CometFallEvent:

    def __init__(self, game) -> None:
        self.percent = 0
        self.percent_speed = 5

        self.all_comets = Group()
        self.game = game

        self.fall_mode = False

    def add_percent(self) -> None:
        self.percent += self.percent_speed / 100

    def is_full_loaded(self) -> bool:
        return self.percent >= 100

    def comet_fall(self):

        for i in range(1, 10):
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.group_monsters) == 0:
            print("Comets are falling")
            self.comet_fall()
            self.fall_mode = True

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface):

        self.add_percent()



        back_bar_color = (83, 83, 83)
        pygame.draw.rect(surface, back_bar_color,
        [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])
        bar_color = (113, 237, 247)
        pygame.draw.rect(surface, bar_color,
        [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])

