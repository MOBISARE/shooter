import os


# Constants for all paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECTILE_PATH = os.path.join(ROOT_DIR, "assets", "projectile.png")
BACKGROUND_PATH = os.path.join(ROOT_DIR, "assets", "bg.jpg")
PLAYER_PATH = os.path.join(ROOT_DIR, "assets", "player.png")
# Constants for the screen

FRAME = 60

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

LEFT_EDGE = -40
RIGHT_EDGE = 920

LEFT_OUT = -100
RIGHT_OUT = 1080

# Constants for the projectile

PROJECTILE_SIZE = 50
PROJECTILE_SCALE_X = 130
PROJECTILE_SCALE_Y = 80
PROJECTILE_VELOCITY = 5
PROJECTILE_ROTATION = 12