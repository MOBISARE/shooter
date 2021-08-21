import constants
from monster import Monster


class Alien(Monster):

    def __init__(self, game) -> None:
        super().__init__(game, "alien", constants.ALIEN_SIZE, constants.ALIEN_OFFSET)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8
