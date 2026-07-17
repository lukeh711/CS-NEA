import pygame

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
    def __init__(self, positionIn, widthIn, heightIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0)):
        self.position = positionIn
        self.width = widthIn
        self.height = heightIn
    
    def move(self, positionIn):
        self.position += positionIn