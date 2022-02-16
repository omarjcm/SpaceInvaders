import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/user.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()
        self.health_start = 50
        self.health_remaining = 50

        self.game = game

    def update(self):
        speed = 3
        cooldown = 100
        current_time = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        self.game.gameover = 0

        pygame.draw.rect(self.game.screen, (0,0,0), (self.rect.x, self.rect.bottom, self.rect.width, 10))

        if self.health_remaining > 0:
            pygame.draw.rect( self.game.screen, (0, 255, 0), (self.rect.x, self.rect.bottom, int( self.rect.width * (self.health_remaining/self.health_start) ), 10))
        elif self.health_remaining == 0:
            self.kill()
            self.game.gameover = 1
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < self.game.window_width:
            self.rect.x += speed

        if key[pygame.K_SPACE] and current_time - self.last_shot > cooldown:
            bullet = Player_Bullet(self.rect.centerx, self.rect.top, self.game)
            self.game.player_bullets_group.add( bullet )
            self.last_shot = pygame.time.get_ticks()

class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/user_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.game = game

    def update(self):
        self.rect.y -= 5
        if pygame.sprite.spritecollide(self, self.game.invaders_group, True):
            self.kill()