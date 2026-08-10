import pygame   # 2 temps
from vector import *
from render import *
from objects import *
from simulation import *


class Game:
    running = True
    simulationSpeed = 1.0   # the overall speed of the simulation (inc. negative numbers for rewinding)
    simulationSpeedAmmount = 1.5    # the ammount the simulations speed is multiplied and divided by each button press
    simulationOperations = 0
    simulationPaused = False

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
        "fullStop": False,
        "comma": False,
        "r": False
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
        "fullStop": False,
        "comma": False,
        "r": False
    }

    #---code run at startup---
    def start(self):    #--0--#
        self.screen = pygame.display.set_mode((1280, 720))                          # (1280, 720)
        self.camera = Camera(self.screen.get_width(), self.screen.get_height())     # (1920, 1080)
        self.render = Render(self.camera, self.screen)                              # (2560, 1440)
        self.simulation = Simulation()                                              # (3840, 2160)

        # add some initial objects into simulation.py
        testPlanet1 = Planet(objectIDIn = 0, velocityIn=Vector(0, 1), positionIn=Vector(-1,0), radiusIn=0.1, massIn=3.003e-6)
        testPlanet2 = Planet(objectIDIn = 1, velocityIn=Vector(0, -1), positionIn=Vector(1,0), radiusIn=0.1, massIn=3.003e-6, colourIn="red")
        testPlanet3 = Planet(objectIDIn = 2, velocityIn=Vector(0, 0), positionIn=Vector(0,0), radiusIn=0.3, massIn=1.0, colourIn="orange")
        self.simulation.addObject(testPlanet1)
        self.simulation.addObject(testPlanet2)
        self.simulation.addObject(testPlanet3)
    

    #---keyboard inputs---
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
                elif event.key == pygame.K_UP or event.key == pygame.K_w:       # up arrow / w
                    self.keyDict["up"] = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:     # left arrow / a
                    self.keyDict["left"] = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:     # down arrow / s
                    self.keyDict["down"] = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:    # right arrow / d
                    self.keyDict["right"] = True
                elif event.key == pygame.K_EQUALS:                  # +
                    self.keyDict["plus"] = True
                elif event.key == pygame.K_MINUS:                   # -
                    self.keyDict["minus"] = True
                elif event.key == pygame.K_LSHIFT:                  # shift
                    self.keyDict["shift"] = True
                elif event.key == pygame.K_LCTRL:                   # ctrl
                    self.keyDict["ctrl"] = True
                elif event.key == pygame.K_PERIOD:                  # .
                    self.keyDict["fullStop"] = True
                elif event.key == pygame.K_COMMA:                   # ,
                    self.keyDict["comma"] = True
                elif event.key == pygame.K_r:                       # r
                    self.keyDict["r"] = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:                     # space
                    self.keyDict["space"] = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:       # up arrow / w
                    self.keyDict["up"] = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:     # left arrow / a
                    self.keyDict["left"] = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:     # down arrow / s
                    self.keyDict["down"] = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:    # right arrow / d
                    self.keyDict["right"] = False
                elif event.key == pygame.K_EQUALS:                  # + and =
                    self.keyDict["plus"] = False
                elif event.key == pygame.K_MINUS:                   # - and _
                    self.keyDict["minus"] = False
                elif event.key == pygame.K_LSHIFT:                  # shift
                    self.keyDict["shift"] = False
                elif event.key == pygame.K_LCTRL:                   # ctrl
                    self.keyDict["ctrl"] = False
                elif event.key == pygame.K_PERIOD:                  # > and .
                    self.keyDict["fullStop"] = False
                elif event.key == pygame.K_COMMA:                   # < and ,
                    self.keyDict["comma"] = False
                elif event.key == pygame.K_r:                       # r
                    self.keyDict["r"] = False


    #---main code---
    def update(self, dt):   #--2--#
        # KEY PRESS LOGIC
        # camera movement
        if self.keyDict["left"]:
            self.camera.move(Vector(-self.camera.movementSpeed, 0) * dt)
        if self.keyDict["right"]:
            self.camera.move(Vector(self.camera.movementSpeed, 0) * dt)
        if self.keyDict["up"]:
            self.camera.move(Vector(0, self.camera.movementSpeed) * dt)
        if self.keyDict["down"]:
            self.camera.move(Vector(0, -self.camera.movementSpeed) * dt)

        # camera zoom control
        if self.keyDict["plus"] and not self.lastFrameKeyDict["plus"]:
            self.camera.zoomIn()
        if self.keyDict["minus"] and not self.lastFrameKeyDict["minus"]:
            self.camera.zoomOut()

        # keys allowing slower or faster camera movement while held down
        if self.keyDict["shift"] and not self.lastFrameKeyDict["shift"]:
            self.camera.movementSpeed *= 5
        elif self.lastFrameKeyDict["shift"] and not self.keyDict["shift"]:
            self.camera.movementSpeed /= 5

        if self.keyDict["ctrl"] and not self.lastFrameKeyDict["ctrl"]:
            self.camera.movementSpeed /= 5
        elif self.lastFrameKeyDict["ctrl"] and not self.keyDict["ctrl"]:
            self.camera.movementSpeed *= 5

        # speeding up or slowing down simulation speed
        if self.keyDict["fullStop"] and not self.lastFrameKeyDict["fullStop"]:
            self.simulationSpeed *= self.simulationSpeedAmmount
        elif self.keyDict["comma"] and not self.lastFrameKeyDict["comma"]:
            self.simulationSpeed /= self.simulationSpeedAmmount

        # toggling rewind
        if self.keyDict["r"] and not self.lastFrameKeyDict["r"]:
            self.simulation.flipVelocities()

        # pausing simulation (toggle)
        if self.keyDict["space"] and not self.lastFrameKeyDict["space"]:
            if self.simulationPaused == True:
                self.simulationPaused = False
            else:
                self.simulationPaused = True
        
        
        # SIMULATION LOGIC
        if not self.simulationPaused:
            self.simulationOperations += self.simulationSpeed
            while self.simulationOperations >= 1:     # adds the fractional speed to the accumulator (operations) each frame, and over time will perform correct number of operations each frame
                self.simulation.tick(dt)
                self.simulationOperations -= 1
        # TEMP: remove prints
        # print(f"CAMERA: Displacement: {self.camera.displacement}, centre: {self.camera.centre}, zoom: {self.camera.zoom}, width: {self.camera.width}, height: {self.camera.height}")
        # print(f"Simulation speed: {self.simulationSpeed}")


    #---rendering code---
    def draw(self):     #--3--#
        # clear last screen
        self.render.fill("black")

        # draw stuff here
        for currentObject in self.simulation.objectList:
            self.render.renderObject(currentObject)

        # send the new frame to the screen
        pygame.display.flip()