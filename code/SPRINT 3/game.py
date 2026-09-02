import pygame   # 2 temps
from vector import *
from render import *
from objects import *
from simulation import *
from UI import *


class Game:
    _running = True
    _framerate = 60

    # dict of all keys pressed last frame
    _lastFrameKeyDict = {
        "leftMouse": False,
        "middleMouse": False,
        "rightMouse": False,
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
    _keyDict = {
        "leftMouse": False,
        "middleMouse": False,
        "rightMouse": False,
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

    # (1280, 720)
    # (1920, 1080)
    # (2560, 1440)
    # (3840, 2160)

    #---code run at startup---
    def start(self):    #--0--#
        # initialise system objects
        self._screen = pygame.display.set_mode((1280, 720))
        self._camera = Camera(self._screen.get_width(), self._screen.get_height())
        self._render = Render(self._camera, self._screen)
        self._simulation = Simulation()
        self._UI = UI(self._screen, self._simulation)

        # create the UI elements
        self._UI.createUI()

        # add some initial objects into simulation.py
        testPlanet1 = Planet(IDIn = 0, velocityIn=Vector(0, 1), positionIn=Vector(-1,0), radiusIn=0.1, massIn=3.003e-6)
        testPlanet2 = Planet(IDIn = 1, velocityIn=Vector(0, -1), positionIn=Vector(1,0), radiusIn=0.1, massIn=3.003e-6, colourIn="red")
        testPlanet3 = Planet(IDIn = 2, velocityIn=Vector(0, 0), positionIn=Vector(0,0), radiusIn=0.3, massIn=1.0, colourIn="orange")
        self._simulation.addObject(testPlanet1)
        self._simulation.addObject(testPlanet2)
        self._simulation.addObject(testPlanet3)
    

    #---keyboard inputs---
    def handleEvents(self): #--1--#
        # shifting all current values to old values
        for i, key in enumerate(self._keyDict):
            self._lastFrameKeyDict[key] = self._keyDict[key]

        # loops through each event
        for event in pygame.event.get():
            # handle UI events first
            self._UI.handleEvents(event)

            # closing nicely when X button pressed
            if event.type == pygame.QUIT:
                self._running = False

            # key press detection
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                    # escape
                    # TEMP: closes when escape is pressed
                    self._running = False
                elif event.key == pygame.K_SPACE:                   # space
                    self._keyDict["space"] = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:       # up arrow / w
                    self._keyDict["up"] = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:     # left arrow / a
                    self._keyDict["left"] = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:     # down arrow / s
                    self._keyDict["down"] = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:    # right arrow / d
                    self._keyDict["right"] = True
                elif event.key == pygame.K_EQUALS:                  # +
                    self._keyDict["plus"] = True
                elif event.key == pygame.K_MINUS:                   # -
                    self._keyDict["minus"] = True
                elif event.key == pygame.K_LSHIFT:                  # shift
                    self._keyDict["shift"] = True
                elif event.key == pygame.K_LCTRL:                   # ctrl
                    self._keyDict["ctrl"] = True
                elif event.key == pygame.K_PERIOD:                  # .
                    self._keyDict["fullStop"] = True
                elif event.key == pygame.K_COMMA:                   # ,
                    self._keyDict["comma"] = True
                elif event.key == pygame.K_r:                       # r
                    self._keyDict["r"] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:                     # space
                    self._keyDict["space"] = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:       # up arrow / w
                    self._keyDict["up"] = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:     # left arrow / a
                    self._keyDict["left"] = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:     # down arrow / s
                    self._keyDict["down"] = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:    # right arrow / d
                    self._keyDict["right"] = False
                elif event.key == pygame.K_EQUALS:                  # + and =
                    self._keyDict["plus"] = False
                elif event.key == pygame.K_MINUS:                   # - and _
                    self._keyDict["minus"] = False
                elif event.key == pygame.K_LSHIFT:                  # shift
                    self._keyDict["shift"] = False
                elif event.key == pygame.K_LCTRL:                   # ctrl
                    self._keyDict["ctrl"] = False
                elif event.key == pygame.K_PERIOD:                  # > and .
                    self._keyDict["fullStop"] = False
                elif event.key == pygame.K_COMMA:                   # < and ,
                    self._keyDict["comma"] = False
                elif event.key == pygame.K_r:                       # r
                    self._keyDict["r"] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._keyDict["leftMouse"] = True
                elif event.button == 2:
                    self._keyDict["middleMouse"] = True
                elif event.button == 3:
                    self._keyDict["rightMouse"] = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self._keyDict["leftMouse"] = False
                elif event.button == 2:
                    self._keyDict["middleMouse"] = False
                elif event.button == 3:
                    self._keyDict["rightMouse"] = False

            elif event.type == pygame.MOUSEMOTION:
                # make mousePosition and mouseMotion for screen and simulation, and mouseMotionButtons for what buttons were pressed while moving the mouse
                # NOTE: mouseMotionButtons is seperate from leftMouse/middleMouse/rightMouse, as mouseMotionButtons only updates when the mouse is moving
                mousePositionScreenTuple = event.pos
                self.mousePositionScreen = Vector(*mousePositionScreenTuple)
                self.mousePosition = self._render.screenToSimulationCoords(self.mousePositionScreen)
                mouseMotionScreen = event.rel
                self.mouseMotionScreen = Vector(*mouseMotionScreen)
                self.mouseMotion = self._render.screenToSimulationMotion(self.mouseMotionScreen)
                self.mouseMotionButtons = event.buttons

        # self.mouseButtonsPressed = pygame.mouse.get_pressed(3)
        # mousePositionScreenTuple = pygame.mouse.get_pos()
        # self.mousePositionScreen = Vector(*mousePositionScreenTuple)
        # self.mousePosition = self._render.screenToSimulationCoords(self.mousePositionScreen)
        # print(self.mousePosition)


    #---main code---
    def update(self, dt):   #--2--#
        # KEY PRESS LOGIC
        # camera movement
        if self._keyDict["left"]:
            self._camera.move(Vector(-self._camera._movementSpeed, 0) * dt)
        if self._keyDict["right"]:
            self._camera.move(Vector(self._camera._movementSpeed, 0) * dt)
        if self._keyDict["up"]:
            self._camera.move(Vector(0, self._camera._movementSpeed) * dt)
        if self._keyDict["down"]:
            self._camera.move(Vector(0, -self._camera._movementSpeed) * dt)

        # camera zoom control
        if self._keyDict["plus"] and not self._lastFrameKeyDict["plus"]:
            self._camera.zoomIn()
        if self._keyDict["minus"] and not self._lastFrameKeyDict["minus"]:
            self._camera.zoomOut()

        # keys allowing slower or faster camera movement while held down
        if self._keyDict["shift"] and not self._lastFrameKeyDict["shift"]:
            self._camera.speedUp(5)
        elif self._lastFrameKeyDict["shift"] and not self._keyDict["shift"]:
            self._camera.speedDown(5)

        if self._keyDict["ctrl"] and not self._lastFrameKeyDict["ctrl"]:
            self._camera.speedDown(5)
        elif self._lastFrameKeyDict["ctrl"] and not self._keyDict["ctrl"]:
            self._camera.speedUp(5)

        # speeding up or slowing down simulation speed
        if self._keyDict["fullStop"] and not self._lastFrameKeyDict["fullStop"]:
            self._simulation.speedUp()
        elif self._keyDict["comma"] and not self._lastFrameKeyDict["comma"]:
            self._simulation.speedDown()

        # toggling rewind
        if self._keyDict["r"] and not self._lastFrameKeyDict["r"]:
            self._simulation.reverse()

        # pausing simulation (toggle)
        if self._keyDict["space"] and not self._lastFrameKeyDict["space"]:
            self._simulation.pauseToggle()

        if self._keyDict["leftMouse"] and not self._lastFrameKeyDict["leftMouse"]:
            if not self._UI.mouseOnUI(self.mousePositionScreen):
                self._simulation.selectionDetection(self.mousePosition, self._UI)

        # ensuring long pauses from breakpoints or window movement doesn't break the physics engine
        if dt > 0.2:
            dt = 0.2
        
        # SIMULATION LOGIC
        self._simulation.frame(dt, self.framerate)
        # TEMP: remove prints
        # print(f"CAMERA: Displacement: {self._camera.displacement}, centre: {self._camera.centre}, zoom: {self._camera.zoom}, width: {self._camera.width}, height: {self._camera.height}")
        # print(f"Simulation speed: {self._simulationSpeed}")

        self._UI.update(dt)


    #---rendering code---
    def draw(self):     #--3--#
        # clear last screen
        self._render.background()

        # draw simulation objects
        for currentObject in self._simulation.objectList:
            self._render.renderObject(currentObject)

        # draw the UI
        self._UI.drawUI()

        # send the new frame to the screen
        pygame.display.flip()

    @property
    def running(self):
        return self._running

    @property
    def framerate(self):
        return self._framerate