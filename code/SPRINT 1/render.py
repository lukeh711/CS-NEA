import pygame
# NOTE: limited imports here to stop circular imports

class Render:
    def __init__(self, cameraIn, screenIn):
        self.camera = cameraIn
        self.screen = screenIn

    # just draws shapes on the screen given the vector coords of those shapes
    def fill(self, colour):
        self.screen.fill(colour)
    
    def circle(self, position, radius, colour):
        centre = position + pygame.Vector2(radius, radius)
        pygame.draw.circle(self.screen, colour, centre, radius)

    def planet(self, planet):
        position = planet.position
        radius = planet.radius
        colour = planet.colour
        self.circle(position, radius, colour)
    
