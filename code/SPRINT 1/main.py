import pygame
from game import *

# initialise pygame screen, and camera and renderer objects
pygame.init()
clock = pygame.time.Clock()
dt = clock.tick(60)
game = Game()


# main game loop
running = True
while game.running:
    # get keyboard inputs
    game.handleEvents()

    game.update(dt)

    game.draw()

    # next frame
    dt = clock.tick(60)

pygame.quit()