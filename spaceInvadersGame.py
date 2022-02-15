import pygame
import random
from invader import *
from player import *

class Game:
    screen = None
    window_height = 600
    window_width = 800

    gameover = 0

    rows = 3
    cols = 10

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.timer = pygame.time.get_ticks()

        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption( 'Space Invaders' )

        self.background = pygame.image.load('./images/background.jpg')

        self.invaders_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.invader_bullets_group = pygame.sprite.Group()
        self.player_bullets_group = pygame.sprite.Group()

        self.create_invaders()

        self.player = Player(int(self.window_width/2), self.window_height - 10, self)
        self.player_group.add( self.player )

        game = True
        while game:
            self.clock.tick(60)
            self.screen.blit( self.background, (0,0) )

            if len(self.invaders_group) == 0:
                self.gameover = 1

            if self.gameover == 0:
                seconds = (pygame.time.get_ticks() - self.timer) / 1000
                if seconds > 5:
                    self.create_invader_bullets()
                    self.timer = pygame.time.get_ticks()

                self.invaders_group.update()
                self.player_group.update()
                self.invader_bullets_group.update()
                self.player_bullets_group.update()

                self.invaders_group.draw( self.screen )
                self.player_group.draw( self.screen )
                self.invader_bullets_group.draw( self.screen )
                self.player_bullets_group.draw( self.screen )

                self.player.update()

            elif self.gameover == 1:
                self.background = pygame.image.load('./images/gameover_background.jpg')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            pygame.display.update()

        pygame.quit()

    def create_invaders(self):
        for row in range(self.rows):
            for col in range(self.cols):
                invader = Invader(self, 100 + col * 65, 80 + row * 50)
                self.invaders_group.add( invader )

    def create_invader_bullets(self):
        attacking_invader = random.choice( self.invaders_group.sprites() )
        invader_bullet = Invader_Bullet( self, attacking_invader.rect.centerx, attacking_invader.rect.centery )
        self.invader_bullets_group.add( invader_bullet )

if __name__ == '__main__':
    game = Game()