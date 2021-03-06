import pygame
import os
from pygame.sprite import Sprite

import constants


class AnimateSprite(Sprite):

    def __init__(self, sprite_name, size=constants.DEFAULT_SIZE):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(os.path.join(constants.ROOT_DIR, "assets", sprite_name) + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop: bool = False):

        if self.animation:

            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0

                if loop is False:
                    self.animation = False

            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


def load_animation_images(sprite_name) -> list:
    images = []
    path = os.path.join(constants.ROOT_DIR, "assets", sprite_name) + f"/{sprite_name}"

    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    return images


animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien")
}
