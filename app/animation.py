import pygame
from pygame.sprite import Sprite

import constants


class AnimateSprite(Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(constants.ASSETS_PATH + sprite_name + constants.PNG)
