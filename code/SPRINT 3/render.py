import pygame
from objects import *

class Render:
    def __init__(self, cameraIn, screenIn):
        self._camera = cameraIn
        self._screen = screenIn

        # load, darken and store the bg image
        brightness = 0.4
        backgroundImage = pygame.image.load("assets/StarsTexture.jpg")
        backgroundImageDarkened = self._darkenImage(backgroundImage, brightness)
        backgroundImageScaled = pygame.transform.scale(backgroundImageDarkened, (self._screen.get_width(), self._screen.get_height()))
        self._bg = backgroundImageScaled

    def _darkenImage(self, image, darkness):
        value = int(darkness * 255)
        copy = image.copy()
        copy.fill((value, value, value), special_flags=pygame.BLEND_RGB_MULT)
        return copy

    def background(self):
        self._screen.blit(self._bg, (0,0))

    # just draws shapes on the screen given the vector coords of those shapes and their dimentions
    def fill(self, colour):
        self._screen.fill(colour)
    
    def _circle(self, positionIn, radius, colour):
        # makes sure the planet can't dissapear entirely from being too small
        radius = max(1, radius)
        centre = (positionIn.getX(), positionIn.getY())

        # only renders it if it is currently within the bounds of the screen
        if (
            centre[0] - radius < self._screen.get_width() and
            centre[1] - radius < self._screen.get_height() and
            centre[0] + radius > 0 and
            centre[1] + radius > 0
        ):
            pygame.draw.circle(self._screen, colour, centre, radius)



    def _planet(self, planet):
        # changing simulation coordinates to rendering coordinates
        # find displacement from centre, times that by the zoom then align it back so it renders from bottom left not centre
        position = ((planet.position - self._camera.centre) * self._camera.zoom) + self._camera.screenCentreOffset
        position = Vector(position.getX(), -position.getY()) + Vector(0, self._screen.get_height())

        # scaling planet's size based on zoom
        radius = planet.radius * self._camera.zoom

        colour = planet.colour
        self._circle(position, radius, colour)
    
    # takes in any supported object and renders it based on the object type
    def renderObject(self, objectIn):
        if isinstance(objectIn, Planet):
            self._planet(objectIn)
        else:
            print(f"Tried to render unsupported object: {objectIn} of type {type(objectIn)}")