import pygame
from game import *

# initialise pygame screen, and camera and renderer objects
pygame.init()
clock = pygame.time.Clock()
dt = 0
game = Game()


# main game loop
running = True
while game.running:
    # get keyboard inputs
    game.handleEvents()

    game.update(dt)

    game.draw()

    # next frame
    dt = clock.tick(1) / 1000

pygame.quit()