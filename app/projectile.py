import pygame.sprite


class Projectile(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, player) -> None:
        super().__init__()

        # Constants
        self.WIDTH = 50
        self.HEIGHT = self.WIDTH
        self.SCALE_X = 130
        self.SCALE_Y = 80
        self.OUT_RIGHT = 1080
        self.OUT_LEFT = -100
        self.player = player
        self.velocity = 5
        self.image = pygame.image.load("/home/mobisare/Documents/PyCharmProjects/shooter/app/assets/projectile.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect.x = player.rect.x + self.SCALE_X
        self.rect.y = player.rect.y + self.SCALE_Y
        self.origin_image = self.image
        self.angle = 0

    def move(self) -> None:
        self.rect.x += self.velocity
        self.rotate()

        if self.rect.x > self.OUT_RIGHT:
            self.remove()

    def remove(self) -> None:
        self.player.all_projectiles.remove(self)

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        #self.rect = self.image.get_rect(center=self.rect.center)


