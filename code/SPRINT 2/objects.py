import pygame

# BASE PHYSICS OBJECT
class PhysicsObject:
    # newPosition = pygame.Vector2(0,0)
    forceList = []
    resultantForce = pygame.Vector2(0,0)
    acceleration = pygame.Vector2(0, 0)

    def __init__(self, positionIn, radiusIn, velocityIn=pygame.Vector2(0, 0), massIn=0):
        self.position = positionIn          # top left position vector
        self.radius = radiusIn              # radius
        self.mass = massIn                  # mass
        self.velocity = velocityIn          # (optional) velocity vector


# PLANET
class Planet(PhysicsObject):
    def __init__(self, positionIn, radiusIn, velocityIn=pygame.Vector2(0, 0), massIn=6e24, colourIn="blue"):
        super().__init__(positionIn, radiusIn, velocityIn, massIn)
        self.colour = colourIn              # colour


# CAMERA
class Camera:
    movementSpeed = 200
    displacement = pygame.Vector2(0, 0)
    zoom = 1.0
    zoomAmmount = 1.2

    def __init__(self, positionIn, widthIn, heightIn):
        self.position = positionIn
        self.initialWidth = widthIn
        self.width = widthIn
        self.initialHeight = heightIn
        self.height = heightIn
        self.initialCentre = pygame.Vector2(widthIn//2, heightIn//2)
        self.centre = pygame.Vector2(widthIn//2, heightIn//2)

    def move(self, positionIn):
        self.position += positionIn
        self.centre += positionIn
        self.displacement += positionIn
    
    def zoomIn(self):
        self.zoom *= self.zoomAmmount
        # reduce the effect of floating point errors by rounding to 6dp
        self.zoom = round(self.zoom, 6)
        self.zoomLogic()
    
    def zoomOut(self):
        self.zoom /= self.zoomAmmount
        # reduce the effect of floating point errors by rounding to 6dp
        self.zoom = round(self.zoom, 8)
        self.zoomLogic()
        

    def zoomLogic(self):
        # change size of camera object
        self.width = self.initialWidth * (1 / self.zoom)
        self.height = self.initialHeight * (1 / self.zoom)