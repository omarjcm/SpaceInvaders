import pygame
from invader import *
from player import *

pygame.init()

window_height = 600
window_width = 800

rows = 3
cols = 10

clock = pygame.time.Clock()

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption( 'Space Invaders' )

background = pygame.image.load('./images/background.jpg')

invaders_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

invader_bullets_group = pygame.sprite.Group()
player_bullets_group = pygame.sprite.Group()

def create_invaders():
    for row in range(rows):
        for col in range(cols):
            invader = Invader(100 + col * 65, 80 + row * 50)
            invaders_group.add( invader )


create_invaders()

player = Player(int(window_width/2), window_height - 10, window_width)
player_group.add( player )

game = True
while game:
    clock.tick(60)

    screen.blit( background, (0,0) )

    invaders_group.update()
    player_group.update()
    invader_bullets_group.update()
    player_bullets_group.update()

    invaders_group.draw( screen )
    player_group.draw( screen )
    invader_bullets_group.draw( screen )
    player_bullets_group.draw( screen )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()

pygame.quit()