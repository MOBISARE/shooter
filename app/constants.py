import os

# Constants for all paths
from typing import Final

ROOT_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))

PROJECTILE_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "projectile.png")
BACKGROUND_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "bg.jpg")
PLAYER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "player.png")
MONSTER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "mummy.png")
BANNER_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "banner.png")
BUTTON_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "button.png")
COMET_PATH: Final[str] = os.path.join(ROOT_DIR, "assets", "comet.png")
# Constants for the screen

FRAME: Final[int] = 60

SCREEN_WIDTH: Final[int] = 1080
SCREEN_HEIGHT: Final[int] = 720

LEFT_EDGE: Final[int] = -40
RIGHT_EDGE: Final[int] = 920

LEFT_OUT: Final[int] = -100
RIGHT_OUT: Final[int] = 1080

GROUND = 500

# Constants for the projectile

PROJECTILE_SIZE: Final[int] = 50
PROJECTILE_SCALE_X: Final[int] = 130
PROJECTILE_SCALE_Y: Final[int] = 80
PROJECTILE_VELOCITY: Final[int] = 5
PROJECTILE_ROTATION: Final[int] = 12
