import pygame

# BASE PHYSICS OBJECT
class PhysicsObject:
    screenHeight = 0
    def __init__(self, positionIn, radiusIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0), massIn=0):
        # self.position = positionIn - pygame.Vector2(0, self.screenHeight)   # bottom left position vector
        self.position = positionIn          # top left position vector
        self.radius = radiusIn              # radius
        self.mass = massIn                  # mass
        self.force = forceIn                # (optional) force vector
        self.velocity = velocityIn          # (optional) velocity vector
        self.acceleration = accelerationIn  # (optional) acceleration vector


# PLANET
class Planet(PhysicsObject):
    def __init__(self, positionIn, radiusIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0), massIn=6e24, colourIn="blue"):
        super().__init__(positionIn, radiusIn, forceIn, velocityIn, accelerationIn, massIn)
        self.colour = colourIn


# CAMERA
class Camera:
    movementSpeed = 100
    displacement = pygame.Vector2(0, 0)
    centre = pygame.Vector2(0, 0)
    zoom = 1.0
    zoomAmmount = 1.1

    def __init__(self, positionIn, widthIn, heightIn):
        self.position = positionIn
        self.initialWidth = widthIn
        self.width = widthIn
        self.initialHeight = heightIn
        self.height = heightIn
    
    def move(self, positionIn):
        self.position += positionIn
        self.centre += positionIn
        self.displacement += positionIn
    
    def zoomIn(self):
        self.zoom *= self.zoomAmmount
        self.zoom = round(self.zoom, 6)
        self.zoomLogic()
    
    def zoomOut(self):
        self.zoom /= self.zoomAmmount
        self.zoom = round(self.zoom, 8)
        self.zoomLogic()
        

    def zoomLogic(self):
        # change size of camera and move camera to same relative place in simulation
        self.width = self.initialWidth * (1 / self.zoom)
        self.height = self.initialHeight * (1 / self.zoom)

        # scaling anchor point from origin
        # self.centre *= self.zoom
        # self.width = self.initialWidth * (1 / self.zoom)
        # self.height = self.initialHeight * (1 / self.zoom)
        # self.position = self.centre + pygame.Vector2(-self.width / 2, self.height / 2)
        # self.displacement = self.centre + pygame.Vector2(-self.width / 2, -self.height / 2)

        # halfWidthDifference = (self.initialWidth - self.width) / 2
        # halfHeightDifference = (self.initialHeight - self.height) / 2
        # self.position -= pygame.Vector2(halfWidthDifference, halfHeightDifference)
        # self.displacement -= pygame.Vector2(halfWidthDifference, -halfHeightDifference)

#         print(f'''
# ~~~
# Before move:
# zoom: {self.zoom}
# initialWidth: {self.initialWidth}
# width: {self.width}
# initialHeight: {self.initialHeight}
# height: {self.height}
# position: {self.position}
# initialPosition: {self.initialPosition}
# displacement: {self.displacement}
# initialDisplacement: {self.initialDisplacement}''')