import pygame
from render import *
from objects import *
from simulation import *


class Game:
    running = True

    # dict of all keys pressed last frame
    lastFrameKeyDict = {
        "space": False,
        "shift": False,
        "ctrl": False,
        "left": False,
        "right": False,
        "up": False,
        "down": False,
        "plus": False,
        "minus": False,
    }

    # dict of all keys pressed this frame
    keyDict = {
        "space": False,
        "shift": False,
        "ctrl": False,
        "left": False,
        "right": False,
        "up": False,
        "down": False,
        "plus": False,
        "minus": False,
    }
    # (1280, 720)
    screen = pygame.display.set_mode((1920, 1080))
    camera = Camera(pygame.Vector2(0, screen.get_height()), screen.get_width(), screen.get_height())
    render = Render(camera, screen)
    simulation = Simulation()
    # list of all objects in the simulation space


    def start(self):    #--0--#
        # add some initial objects into simulation.py
        testPlanet1 = Planet(objectIDIn = 0, velocityIn=pygame.Vector2(0, 90), positionIn=pygame.Vector2(1000,600), radiusIn=10, massIn=5.972e24)
        testPlanet2 = Planet(objectIDIn = 1, velocityIn=pygame.Vector2(0, -50), positionIn=pygame.Vector2(500,600), radiusIn=10, massIn=5.972e24, colourIn="red")
        testPlanet3 = Planet(objectIDIn = 2, velocityIn=pygame.Vector2(0, 0), positionIn=pygame.Vector2(800,600), radiusIn=15, massIn=5.972e25, colourIn="orange")
        self.simulation.addObject(testPlanet1)
        self.simulation.addObject(testPlanet2)
        self.simulation.addObject(testPlanet3)
    

    # keyboard inputs
    def handleEvents(self): #--1--#
        # shifting all current values to old values
        keyList = list(self.keyDict.keys())
        for i, key in enumerate(self.keyDict):
            self.lastFrameKeyDict[key] = self.keyDict[key]

        for event in pygame.event.get():
            # closing nicely when X button pressed
            if event.type == pygame.QUIT:
                self.running = False
            
            # key press detection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                    # escape
                    # TEMP: closes when escape is pressed
                    self.running = False
                elif event.key == pygame.K_SPACE:                   # space
                    self.keyDict["space"] = True
                elif event.key == pygame.K_LEFT:                    # left arrow
                    self.keyDict["left"] = True
                elif event.key == pygame.K_RIGHT:                   # right arrow
                    self.keyDict["right"] = True
                elif event.key == pygame.K_UP:                      # up arrow
                    self.keyDict["up"] = True
                elif event.key == pygame.K_DOWN:                    # down arrow
                    self.keyDict["down"] = True
                elif event.key == pygame.K_EQUALS:                  # +
                    self.keyDict["plus"] = True
                elif event.key == pygame.K_MINUS:                   # -
                    self.keyDict["minus"] = True
                elif event.key == pygame.K_LSHIFT:                  # shift
                    self.keyDict["shift"] = True
                elif event.key == pygame.K_LCTRL:                   # ctrl
                    self.keyDict["ctrl"] = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:                     # space
                    self.keyDict["space"] = False
                elif event.key == pygame.K_LEFT:                    # left arrow
                    self.keyDict["left"] = False
                elif event.key == pygame.K_RIGHT:                   # right arrow
                    self.keyDict["right"] = False
                elif event.key == pygame.K_UP:                      # up arrow
                    self.keyDict["up"] = False
                elif event.key == pygame.K_DOWN:                    # down arrow
                    self.keyDict["down"] = False
                elif event.key == pygame.K_EQUALS:                  # +
                    self.keyDict["plus"] = False
                elif event.key == pygame.K_MINUS:                   # -
                    self.keyDict["minus"] = False
                elif event.key == pygame.K_LSHIFT:                  # shift
                    self.keyDict["shift"] = False
                elif event.key == pygame.K_LCTRL:                   # ctrl
                    self.keyDict["ctrl"] = False


    # main code
    def update(self, dt):   #--2--#
        # key press logic
        if self.keyDict["left"]:
            self.camera.move(pygame.Vector2(-self.camera.movementSpeed, 0) * dt)
        if self.keyDict["right"]:
            self.camera.move(pygame.Vector2(self.camera.movementSpeed, 0) * dt)
        if self.keyDict["up"]:
            self.camera.move(pygame.Vector2(0, self.camera.movementSpeed) * dt)
        if self.keyDict["down"]:
            self.camera.move(pygame.Vector2(0, -self.camera.movementSpeed) * dt)
        if self.keyDict["plus"] and not self.lastFrameKeyDict["plus"]:
            self.camera.zoomIn()
        if self.keyDict["minus"] and not self.lastFrameKeyDict["minus"]:
            self.camera.zoomOut()
        if self.keyDict["shift"] and not self.lastFrameKeyDict["shift"]:
            self.camera.movementSpeed *= 5
        elif self.lastFrameKeyDict["shift"] and not self.keyDict["shift"]:
            self.camera.movementSpeed /= 5
            

        self.simulation.tick(dt)
        print(f"CAMERA: Position: {self.camera.position}, Displacement: {self.camera.displacement}, centre: {self.camera.centre}, zoom: {self.camera.zoom}")


    # rendering code
    def draw(self):     #--3--#
        # clear last screen
        self.render.fill("black")

        # draw stuff here
        for currentObject in self.simulation.objectList:
            self.render.renderObject(currentObject)

        # send the new frame to the screen
        pygame.display.flip()