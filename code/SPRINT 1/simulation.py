import pygame
from render import *
from objects import *
from simulation import *

def simulationLogic(screen, camera, render):
    # KEY PRESS DETECTION
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                testPlanet.colour = "red"
    
    # render.circle((500, 200), 50, "red")

    testPlanet = Planet(positionIn=pygame.Vector2(1000,500), radiusIn=50, massIn=5.972e24)
    render.planet(testPlanet)