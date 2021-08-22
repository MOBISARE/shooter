import constants
from monster import Monster


class Mummy(Monster):

    def __init__(self, game) -> None:
        super().__init__(game, "mummy", constants.MUMMY_SIZE)
        self.set_speed(3)
        self.set_loot_amount(20)

