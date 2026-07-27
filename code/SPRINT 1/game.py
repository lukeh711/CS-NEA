import pygame
from render import *
from objects import *

class Game:
    running = True
    # TODO: split up into two dictionaries
    keyDict = {
        "space": False,
        "oldSpace": False,
        "shift": False,
        "oldShift": False,
        "ctrl": False,
        "oldCtrl": False,
        "left": False,
        "oldLeft": False,
        "right": False,
        "oldRight": False,
        "up": False,
        "oldUp": False,
        "down": False,
        "oldDown": False,
        "plus": False,
        "oldPlus": False,
        "minus": False,
        "oldMinus": False
    }
    screen = pygame.display.set_mode((1920, 1080))
    camera = Camera(pygame.Vector2(0, screen.get_height()), screen.get_width(), screen.get_height())
    render = Render(camera, screen)

    objectList = []

    testPlanet1 = Planet(positionIn=pygame.Vector2(500,500), radiusIn=10, massIn=5.972e24)
    testPlanet2 = Planet(positionIn=pygame.Vector2(300,300), radiusIn=10, massIn=5.972e24)
    testPlanet3 = Planet(positionIn=pygame.Vector2(0,0), radiusIn=10, massIn=5.972e24, colourIn="yellow")
    testPlanet4 = Planet(positionIn=pygame.Vector2(100,-100), radiusIn=10, massIn=5.972e24, colourIn="orange")
    testPlanet5 = Planet(positionIn=pygame.Vector2(-100,-100), radiusIn=10, massIn=5.972e24, colourIn="green")
    testPlanet6 = Planet(positionIn=pygame.Vector2(-100,100), radiusIn=10, massIn=5.972e24, colourIn="blue")
    testPlanet7 = Planet(positionIn=pygame.Vector2(100,100), radiusIn=10, massIn=5.972e24, colourIn="purple")
    testPlanet8 = Planet(positionIn=pygame.Vector2(-300,-500), radiusIn=10, massIn=5.972e24, colourIn="pink")
    objectList.append(testPlanet1)
    objectList.append(testPlanet2)
    objectList.append(testPlanet3)
    objectList.append(testPlanet4)
    objectList.append(testPlanet5)
    objectList.append(testPlanet6)
    objectList.append(testPlanet7)
    objectList.append(testPlanet8)

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
                # elif event.key == pygame.K_:                  # 
                #     self.keyDict[""] = True
                # elif event.key == pygame.K_:                  # 
                #     self.keyDict[""] = True
            
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
                # elif event.key == pygame.K_:                  # 
                #     self.keyDict[""] = False


    # main code
    def update(self, dt):   #--2--#
        if self.keyDict["left"]:
            self.camera.move(pygame.Vector2(-self.camera.movementSpeed, 0) * dt)
        if self.keyDict["right"]:
            self.camera.move(pygame.Vector2(self.camera.movementSpeed, 0) * dt)
        if self.keyDict["up"]:
            self.camera.move(pygame.Vector2(0, self.camera.movementSpeed) * dt)
        if self.keyDict["down"]:
            self.camera.move(pygame.Vector2(0, -self.camera.movementSpeed) * dt)
        if self.keyDict["plus"] and not self.keyDict["oldPlus"]:
            self.camera.zoomIn()
        if self.keyDict["minus"] and not self.keyDict["oldMinus"]:
            self.camera.zoomOut()
        if self.keyDict["shift"] and not self.keyDict["oldShift"]:
            self.camera.movementSpeed *= 5
        elif self.keyDict["oldShift"] and not self.keyDict["shift"]:
            self.camera.movementSpeed /= 5

        # simulation.tick()


        # print(f"CAMERA: Position: {self.camera.position}, Displacement: {self.camera.displacement}, centre: {self.camera.centre}, zoom: {self.camera.zoom}")


    # rendering code
    def draw(self):     #--3--#
        # clear last screen
        self.render.fill("black")

        # draw stuff here
        for currentObject in self.objectList:
            self.render.renderObject(currentObject)

        # send the new frame to the screen
        pygame.display.flip()