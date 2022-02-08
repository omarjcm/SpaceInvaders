from pickle import FALSE
from turtle import window_height, window_width
import pygame

pygame.init()

window_height = 600
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption( 'Space Invaders' )

background = pygame.image.load('./images/background.jpg')

game = True
while game:
    screen.blit( background, (0,0) )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        pygame.display.update()

pygame.quit()