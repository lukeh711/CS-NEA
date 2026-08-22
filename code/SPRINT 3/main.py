import pygame   # 1 temp
from game import *

# initialise pygame screen, and camera and renderer objects
pygame.init()
clock = pygame.time.Clock()
dt = 0
game = Game()
# initialise game variables
game.start()

# main game loop
while game.running:
    # TEMP: remove prints for screenshots
    # print("New frame")

    # get keyboard inputs
    game.handleEvents()

    # update physics & game logic
    game.update(dt)

    # draw items onto the screen
    game.draw()

    # next frame
    dt = clock.tick(game.framerate) / 1000

pygame.quit()