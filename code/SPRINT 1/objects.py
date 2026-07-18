import pygame
import copy

# BASE PHYSICS OBJECT
class PhysicsObject:
    def __init__(self, positionIn, radiusIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0), massIn=0):
        self.position = positionIn                  # top left position vector
        self.radius = radiusIn                      # radius
        self.mass = massIn                          # mass
        self.force = forceIn                        # (optional) force vector
        self.velocity = velocityIn                  # (optional) velocity vector
        self.acceleration = accelerationIn          # (optional) acceleration vector


# PLANET
class Planet(PhysicsObject):
    def __init__(self, positionIn, radiusIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0), massIn=6e24, colourIn="blue"):
        super().__init__(positionIn, radiusIn, forceIn, velocityIn, accelerationIn, massIn)
        self.colour = colourIn


# CAMERA
class Camera:
    movementSpeed = 50
    initialDisplacement = pygame.Vector2(0, 0)
    displacement = pygame.Vector2(0, 0)
    zoom = 1.0
    zoomAmmount = 1.5

    def __init__(self, positionIn, widthIn, heightIn):
        self.initialPosition = copy.deepcopy(positionIn)
        self.position = positionIn
        self.initialWidth = widthIn
        self.width = widthIn
        self.initialHeight = heightIn
        self.height = heightIn
    
    def move(self, positionIn):
        print(f'''
~~~
Before move:
zoom: {self.zoom}
initialWidth: {self.initialWidth}
width: {self.width}
initialHeight: {self.initialHeight}
height: {self.height}
position: {self.position}
initialPosition: {self.initialPosition}
displacement: {self.displacement}
initialDisplacement: {self.initialDisplacement}''')
        self.position += positionIn
        self.displacement += positionIn
        print(f'''
~~~
After move:
zoom: {self.zoom}
initialWidth: {self.initialWidth}
width: {self.width}
initialHeight: {self.initialHeight}
height: {self.height}
position: {self.position}
initialPosition: {self.initialPosition}
displacement: {self.displacement}
initialDisplacement: {self.initialDisplacement}''')
    
    def zoomIn(self):
        print(f'''
+++
Before zoom in:
zoom: {self.zoom}
initialWidth: {self.initialWidth}
width: {self.width}
initialHeight: {self.initialHeight}
height: {self.height}
position: {self.position}
initialPosition: {self.initialPosition}
displacement: {self.displacement}
initialDisplacement: {self.initialDisplacement}''')
        self.zoom *= 1.5
        self.width = self.initialWidth * (1 / self.zoom)
        self.height = self.initialHeight * (1 / self.zoom)
        halfWidthDifference = abs((self.initialWidth - self.width) / 2)
        halfHeightDifference = abs((self.initialHeight - self.height) / 2)
        self.position = self.initialPosition + pygame.Vector2(halfWidthDifference, halfHeightDifference)
        self.displacement = self.initialDisplacement + pygame.Vector2(halfWidthDifference, -1*halfHeightDifference)
        print(f'''
+++
After zoom in:
zoom: {self.zoom}
initialWidth: {self.initialWidth}
width: {self.width}
initialHeight: {self.initialHeight}
height: {self.height}
position: {self.position}
initialPosition: {self.initialPosition}
displacement: {self.displacement}
initialDisplacement: {self.initialDisplacement}''')
    
    def zoomOut(self):
        self.zoom /= self.zoomAmmount
        self.width = self.initialWidth * (1 / self.zoom)
        self.height = self.initialHeight * (1 / self.zoom)
        halfWidthDifference = abs((self.initialWidth - self.width) / 2)
        halfHeightDifference = abs((self.initialHeight - self.height) / 2)
        self.position = self.initialPosition + pygame.Vector2(halfWidthDifference, halfHeightDifference)
        self.displacement = self.initialDisplacement + pygame.Vector2(halfWidthDifference, -1*halfHeightDifference)