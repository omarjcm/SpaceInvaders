import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, window_width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/user.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.window_width = window_width

    def update(self):
        speed = 3
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < self.window_width:
            self.rect.x += speed


class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/user_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5