import pygame


class CometFallEvent:

    def __init__(self) -> None:
        self.percent = 0
        self.percent_speed = 33

    def add_percent(self) -> None:
        self.percent += self.percent_speed / 100

    def is_full_loaded(self) -> bool:
        return self.percent >= 100

    def attempt_fall(self):
        if self.is_full_loaded():
            print("Comets are falling")
            self.reset_percent()

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface):

        self.add_percent()

        self.attempt_fall()

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

