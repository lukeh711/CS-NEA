import pygame
# NOTE: v limited imports here to stop circular imports

class Render:
    def __init__(self, cameraIn, screenIn):
        self.camera = cameraIn
        self.screen = screenIn

    def circle(self, position, radius, colour):
        centre = position + pygame.Vector2(radius, radius)
        pygame.draw.circle(self.screen, colour, centre, radius)