import pygame

import constants


class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound(constants.SOUND_CLICK_PATH),
            "game_over": pygame.mixer.Sound(constants.SOUND_GAME_OVER_PATH),
            "meteorite": pygame.mixer.Sound(constants.SOUND_METEORITE_PATH),
            "tir": pygame.mixer.Sound(constants.SOUND_SHOOT_PATH)
        }

    def play(self, name):
        self.sounds[name].play()