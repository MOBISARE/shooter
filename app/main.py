import pygame
from game import Game

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    Point d'entré du programme.
    """
    print("Launching...")
    pygame.init()
    game = Game()
    game.run()

