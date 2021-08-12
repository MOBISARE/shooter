import pygame
from pygame.sprite import Sprite

import constants


class Comet(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(constants.COMET_PATH)
        self.rect = self.image.get_rect()
