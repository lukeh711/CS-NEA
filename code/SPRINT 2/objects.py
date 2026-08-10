from vector import *

# BASE PHYSICS OBJECT
class PhysicsObject:
    forceDict = {}
    resultantForce = Vector(0,0)
    acceleration = Vector(0, 0)

    def __init__(self, objectIDIn, positionIn, radiusIn, velocityIn=Vector(0, 0), massIn=0):
        self.objectID = objectIDIn          # ID for working with different objects
        self.position = positionIn          # position
        self.radius = radiusIn              # radius
        self.mass = massIn                  # mass
        self.velocity = velocityIn          # (optional) velocity vector


# PLANET
class Planet(PhysicsObject):
    def __init__(self, objectIDIn, positionIn, radiusIn, velocityIn=Vector(0, 0), massIn=6e24, colourIn="blue"):
        super().__init__(objectIDIn, positionIn, radiusIn, velocityIn, massIn)
        self.colour = colourIn              # colour


# CAMERA
class Camera:
    zoom = 1.0
    inverseZoom = 1.0
    zoomAmmount = 1.2   # the * step each zoom in or out takes
    movementSpeed = 200 # the speed of the camera (in arbritrary units) (~200)
    startingWidth = 10  # the target initial starting size of the camera
    startingCentre = Vector(0,0)    # the target initial position for the centre of the camera
    displacement = Vector(0, 0)

    def __init__(self, widthIn, heightIn):
        # stores the width and height of the screen
        self.screenWidth = widthIn
        self.screenHeight = heightIn
        # works out the vector from the bottom left corner to the centre of the screen (used for rendering)
        self.screenCentreOffset = Vector(self.screenWidth//2, self.screenHeight//2)

        self.zoom = widthIn / self.startingWidth # zoom in enough to make the width of the camera match with the startingCentre variable
        self.zoomLogic()

        self.centre = self.startingCentre   # define the new centre based on the startingCentre variable

    def move(self, positionIn):
        self.centre += positionIn * self.inverseZoom
        self.displacement += positionIn * self.inverseZoom
    
    def zoomIn(self):
        self.zoom *= self.zoomAmmount   # no rounding to reduce errors with large zooms in / out, irrespective of small insignificant floating point errors
        self.zoomLogic()
    
    def zoomOut(self):
        self.zoom /= self.zoomAmmount   # no rounding to reduce errors with large zooms in / out, irrespective of small insignificant floating point errors
        self.zoomLogic()

    def zoomLogic(self):
        # calculate inverse zoom ()
        self.inverseZoom = 1 / self.zoom

        # change size of camera object
        self.width = self.screenWidth * self.inverseZoom
        self.height = self.screenHeight * self.inverseZoom