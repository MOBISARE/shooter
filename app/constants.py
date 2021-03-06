import os

# Constants for all paths
from typing import Final, Tuple

ROOT_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))

PROJECTILE_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "projectile.png")
BACKGROUND_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "bg.jpg")
PLAYER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "player.png")
MONSTER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "mummy.png")
BANNER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "banner.png")
BUTTON_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "button.png")
COMET_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "comet.png")
FONT_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "font.ttf")

ASSETS_PATH: Final[str] = os.path.join(ROOT_DIR, "assets")

SOUND_CLICK_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "sounds", "click.ogg")
SOUND_GAME_OVER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "sounds", "game_over.ogg")
SOUND_METEORITE_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "sounds", "meteorite.ogg")
SOUND_SHOOT_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "sounds", "tir.ogg")

PNG: Final[str] = ".png"
# Constants for the screen

FRAME: Final[int] = 60

SCREEN_WIDTH: Final[int] = 1080
SCREEN_HEIGHT: Final[int] = 720

LEFT_EDGE: Final[int] = -40
RIGHT_EDGE: Final[int] = 920

LEFT_OUT: Final[int] = -100
RIGHT_OUT: Final[int] = 1080

GROUND = 500

SCORE_SIZE: Final[int] = 25
TEXT_COLOR: Final[Tuple[int, int, int]] = (255, 255, 255)
SCORE_POSITION: Final[Tuple[int, int]] = (20, 20)

# Constants for the projectile

PROJECTILE_SIZE: Final[int] = 50
PROJECTILE_SCALE_X: Final[int] = 130
PROJECTILE_SCALE_Y: Final[int] = 80
PROJECTILE_VELOCITY: Final[int] = 5
PROJECTILE_ROTATION: Final[int] = 12

# Constants for entities

MUMMY_SIZE: Final[Tuple[int, int]] = (130, 130)
ALIEN_SIZE: Final[Tuple[int, int]] = (300, 300)
DEFAULT_SIZE: Final[Tuple[int, int]] = (200, 200)

# Offset

DEFAULT_OFFSET: int = 0
ALIEN_OFFSET: int = 130

