import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/user.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]