import pygame
from game import *

# initialise pygame screen, and camera and renderer objects
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
camera = Camera(pygame.Vector2(0, 0), 1280, 720)
render = Render(camera, screen)
game = Game()


# main game loop
running = True
while game.running:
    game.handleEvents()
    game.update()
    game.draw()

    # clear last screen
    screen.fill("black")

    game.simulationLogic(screen, camera, render)    

    # next frame
    
    clock.tick(60)

pygame.quit()