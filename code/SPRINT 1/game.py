import pygame
from render import *
from objects import *

class Game:
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
    screen = pygame.display.set_mode((1280, 720))
    camera = Camera(pygame.Vector2(0, 0), 1280, 720)
    render = Render(camera, screen)


    # keyboard inputs
    def handleEvents(self): #--1--#
        # shifting all current values to old values
        keyList = list(self.keyDict.keys())
        for i in range(0, len(keyList), 2):
            self.keyDict[keyList[i+1]] = self.keyDict[keyList[i]]

        for event in pygame.event.get():
            # closing nicely when X button pressed
            if event.type == pygame.QUIT:
                self.running = False
            
            # getting keyboard inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                    # escape
                    # TEMPish: closes when escape is pressed
                    self.running = False
                if event.key == pygame.K_SPACE:                     # space
                    self.keyDict["space"] = True
                if event.key == pygame.K_LEFT:                      # left arrow
                    self.keyDict["left"] = True
                if event.key == pygame.K_RIGHT:                     # right arrow
                    self.keyDict["right"] = True
                if event.key == pygame.K_UP:                        # up arrow
                    self.keyDict["up"] = True
                if event.key == pygame.K_DOWN:                      # down arrow
                    self.keyDict["down"] = True

    # main code
    def update(self, dt):   #--2--#

        if self.keyDict["left"]:
            pass

        # simulation.tick()
        self.testPlanet = Planet(positionIn=pygame.Vector2(1000,500), radiusIn=50, massIn=5.972e24)

    # rendering code
    def draw(self):     #--3--#
        # clear last screen
        self.render.fill("black")

        # draw stuff here
        self.render.planet(self.testPlanet)

        # send the new frame to the screen
        pygame.display.flip()