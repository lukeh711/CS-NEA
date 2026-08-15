from vector import *

# BASE PHYSICS OBJECT
class PhysicsObject:
    forceDict = {}
    resultantForce = Vector(0,0)
    acceleration = Vector(0, 0)
    _selected = False

    def __init__(self, objectIDIn, positionIn, radiusIn, velocityIn=Vector(0, 0), massIn=0):
        self._objectID = objectIDIn          # ID for working with different objects
        self.position = positionIn          # position
        self.radius = radiusIn              # radius
        self.mass = massIn                  # mass
        self.velocity = velocityIn          # (optional) velocity vector

    def select(self):
        pass

    @property
    def selected(self):
        return self._selected

    @property
    def objectID(self):
        return self._objectID


# PLANET
class Planet(PhysicsObject):
    def __init__(self, objectIDIn, positionIn, radiusIn, velocityIn=Vector(0, 0), massIn=6e24, colourIn="blue"):
        super().__init__(objectIDIn, positionIn, radiusIn, velocityIn, massIn)
        self.colour = colourIn              # colour


# CAMERA
class Camera:
    _zoom = 1.0
    _inverseZoom = 1.0
    _zoomIncriment = 1.2   # the * step each zoom in or out takes
    _movementSpeed = 200 # the speed of the camera (in arbritrary units) (~200)
    _startingWidth = 10  # the target initial starting size of the camera
    _startingCentre = Vector(0,0)    # the target initial position for the centre of the camera
    _displacement = Vector(0, 0)

    def __init__(self, widthIn, heightIn):
        # stores the width and height of the screen
        self._screenWidth = widthIn
        self._screenHeight = heightIn
        # works out the vector from the bottom left corner to the centre of the screen (used for rendering)
        self._screenCentreOffset = Vector(self._screenWidth//2, self._screenHeight//2)

        self._zoom = widthIn / self._startingWidth # zoom in enough to make the width of the camera match with the startingCentre variable
        self._zoomLogic()

        self._centre = self._startingCentre   # define the new centre based on the startingCentre variable

    def move(self, positionIn):
        self._centre += positionIn * self._inverseZoom
        self._displacement += positionIn * self._inverseZoom
    
    def zoomIn(self):
        self._zoom *= self._zoomIncriment   # no rounding to reduce errors with large zooms in / out, irrespective of small insignificant floating point errors
        self._zoomLogic()
    
    def zoomOut(self):
        self._zoom /= self._zoomIncriment   # no rounding to reduce errors with large zooms in / out, irrespective of small insignificant floating point errors
        self._zoomLogic()

    def _zoomLogic(self):
        # calculate inverse zoom ()
        self._inverseZoom = 1 / self._zoom

        # change size of camera object
        self._width = self._screenWidth * self._inverseZoom
        self._height = self._screenHeight * self._inverseZoom

    def speedUp(self, speedIncriment):
        self._movementSpeed *= speedIncriment

    def speedDown(self, speedIncriment):
            self._movementSpeed /= speedIncriment

    @property
    def zoom(self):
        return self._zoom

    @property
    def centre(self):
        return self._centre

    @property
    def screenCentreOffset(self):
        return self._screenCentreOffset