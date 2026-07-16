import pygame
from render import *
from objects import *
from simulation import *

# initialise pygame screen, and camera and renderer objects
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
camera = Camera(pygame.Vector2(0, 0), 1280, 720)
render = Render(camera, screen)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                

    # clear last screen
    screen.fill("black")

    simulationLogic(screen, camera, render)    

    # next frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()