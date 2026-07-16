import pygame

# BASIC PHYSICS OBJECT
class PhysicsObject:
    def __init__(self, xIn, yIn, wIn, hIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0), massIn=0):
        self.position = pygame.Vector2(xIn, yIn)    # top left position vector
        self.w = wIn                                # width
        self.h = hIn                                # height
        self.mass = massIn                          # mass
        self.force = forceIn                        # (optional) force vector
        self.velocity = velocityIn                  # (optional) velocity vector
        self.acceleration = accelerationIn          # (optional) acceleration vector

# PLANET
class Planet(PhysicsObject):
    def __init__(self, xIn, yIn, wIn, hIn, forceIn=pygame.Vector2(0, 0), velocityIn=pygame.Vector2(0, 0), accelerationIn=pygame.Vector2(0, 0), massIn=0, colourIn="blue"):
        super().__init__(xIn, yIn, wIn, hIn, forceIn, velocityIn, accelerationIn, massIn)
        self.colour = colourIn


# CAMERA
class Camera:
    def __init__(self, xIn, yIn, wIn, hIn):
        self.position = pygame.Vector2(xIn, yIn)