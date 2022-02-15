import pygame

class Invader( pygame.sprite.Sprite ):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/spaceInvaders.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_direction = 1
        self.move_counter = 0
        self.game = game
    
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1

        if self.move_counter > 75:
            self.move_direction *= -1
            self.move_counter *= -1
        

class Invader_Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/invader_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.game = game

    def update(self):
        self.rect.y += 2

        if pygame.sprite.spritecollide(self, self.game.player_group, False):
            self.kill()
            self.game.player.health_remaining -= 10