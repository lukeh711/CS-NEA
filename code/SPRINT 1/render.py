import pygame
from objects import *
# NOTE: limited imports here to stop circular imports

# TODO: fix zoom position - currently zooms around bottom left hand corner of screen

class Render:
    def __init__(self, cameraIn, screenIn):
        self.camera = cameraIn
        self.screen = screenIn

    # just draws shapes on the screen given the vector coords of those shapes and their dimentions
    def fill(self, colour):
        self.screen.fill(colour)
    
    def circle(self, positionIn, radius, colour):
        # makes sure the planet can't dissapear entirely from being too small
        radius = max(1, radius)
        position = positionIn
        centre = position + pygame.Vector2(radius, -radius)


        if (
            position.x < self.screen.get_width() and
            position.y - (2 * radius) < self.screen.get_height() and
            position.x + (2 * radius) > 0 and
            position.y > 0
        ):
            print(f"{colour} circle rendered")
            pygame.draw.circle(self.screen, colour, centre, radius)



    def planet(self, planet):
        # changing simulation coordinates to rendering coordinates
        position = ((planet.position - self.camera.displacement) * self.camera.zoom)
        position = pygame.Vector2(position.x, -position.y) + pygame.Vector2(0, self.screen.get_height())

        # scaling planet's size based on zoom
        radius = planet.radius * self.camera.zoom

        colour = planet.colour
        self.circle(position, radius, colour)
    
    # takes in any supported object and renders it based on the object type
    def renderObject(self, objectIn):
        if isinstance(objectIn, Planet):
            self.planet(objectIn)
        else:
            print(f"Tried to render unsupported object: {objectIn} of type {type(objectIn)}")