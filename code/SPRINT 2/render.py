import pygame
from objects import *

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

        # only renders it if it is currently within the bounds of the screen
        if (
            position.x < self.screen.get_width() and
            position.y - (2 * radius) < self.screen.get_height() and
            position.x + (2 * radius) > 0 and
            position.y > 0
        ):
            pygame.draw.circle(self.screen, colour, centre, radius)



    def planet(self, planet):
        # changing simulation coordinates to rendering coordinates
        # find displacement from centre, times that by the zoom then align it back so it renders from bottom left not centre
        position = ((planet.position - self.camera.centre) * self.camera.zoom) + self.camera.initialCentre
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