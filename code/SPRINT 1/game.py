import pygame
from render import *
from objects import *

class Game:
    # attributes
    running = True
    keyDict = {
        "space": False,
        "oldSpace": False,
        "left": False,
        "oldLeft": False,
        "right": False,
        "oldRight": False,
        "up": False,
        "oldUp": False,
        "down": False,
        "oldDown": False
    }

    # methods
    def handleEvents(self): #--1--#
        #shifting all current values to old values
        keyList = list(self.keyDict.keys())
        for i in range(0, len(keyList), 2):
            self.keyDict[keyList[i+1]] = self.keyDict[keyList[i]]

        for event in pygame.event.get():
            # closing nicely when X button pressed
            if event.type == pygame.QUIT:
                self.running = False
            
            #getting keyboard inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                    #escape
                    # TEMPish: closes when escape is pressed
                    self.running = False
                if event.key == pygame.K_SPACE:                     #space
                    spaceKeyPressedNow = True
                    if self.spaceKey == 0 and spaceKeyPressedNow:
                        self.spaceKey = 1
                    else:
                        self.spaceKey = 2
                if event.key == pygame.K_LEFT:                      #Left arrow
                    spaceKeyPressedNow = True
                    if self.spaceKey == 0 and spaceKeyPressedNow:
                        self.spaceKey = 1
                    else:
                        self.spaceKey = 2
                if event.key == pygame.K_RIGHT:                     #Right arrow
                    spaceKeyPressedNow = True
                    if self.spaceKey == 0 and spaceKeyPressedNow:
                        self.spaceKey = 1
                    else:
                        self.spaceKey = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    spaceKeyPressedNow = False

    def update(self):   #--2--#
        # all logic here
        running = self.keyPressDetection()
    

    def draw(self):     #--3--#
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