import pygame

class Invader( pygame.sprite.Sprite ):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/spaceInvaders.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]