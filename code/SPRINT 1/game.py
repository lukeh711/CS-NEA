import pygame
from render import *
from objects import *

class Game:
    # attributes
    running = True

    
    def __init__(self):
        pass


    # methods
    def handleEvents(self): #1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False 
                if event.key == pygame.K_SPACE:
                    spaceKeyPressed = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    spaceKeyPressed = False

    def update(self):   #2
        # all logic here
        running = self.keyPressDetection()
    

    def draw(self):     #3
        # draw stuff here
        pygame.display.flip()


    def keyPressDetection(self):
        runningLocal = True
        return runningLocal


    def simulationLogic(self, screen, camera, render):    
        # initialise objects
        testPlanet = Planet(positionIn=pygame.Vector2(1000,500), radiusIn=50, massIn=5.972e24)

        # rendering
        render.planet(testPlanet)