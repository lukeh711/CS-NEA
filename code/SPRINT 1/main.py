import pygame
from render import *
from objects import *

# initialise pygame screen, and camera and renderer objects
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
camera = Camera(0, 0, 1280, 720)
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

    screen.fill("black")

    render.circle((500, 200), 50, "red")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()