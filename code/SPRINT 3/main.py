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
running = True
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
    dt = clock.tick(60) / 1000

pygame.quit()