# update all the physics when simulation.tick() called
# mainly object management and controlling what physics functions are called
# NOTE: no actual maths happens here - that's what physics.py is for!
import pygame
import physics

class Simulation:
    def __init__(self, objectListIn):
        self.objectList = objectListIn

    def addObject():    #add an object to the simulation
        pass

    def removeObject(): #remove an object from the simulation
        pass

    def tick(self):
        # clear each planet's forceList
        for currentObject in self.objectList:
            currentObject.forceList = []    # wipes forceList
            for i in range(len(self.objectList)-1):
                currentObject.forceList.append(pygame.Vector2(0,0)) # adds a (0,0) slot for each other planet in forceList
            print(f"currentObject at {currentObject.position} has this forceList: {currentObject.forceList}")

        # main physics updating all object attributes
        for currentObject in self.objectList:
            self.findForces(currentObject)      # find all forces acting on the object
            self.addForces(currentObject)       # add all the forces together
            self.calcAcceleration(currentObject)# find acceleration from force and mass
            self.calcPosition(currentObject)    # update planet position


    def findForces(self, objectIn):   # find each of the forces effecting current object
        pass    # find force pairs and update both planets force

    def addForces(self, objectIn):
        objectIn.resultantForce = physics.resultantForce(objectIn.forceList)

    def calcAcceleration(self, objectIn):
        objectIn.acceleration = physics.acceleration(objectIn.resultantForce, objectIn.mass)

    def calcPosition(self, objectIn):
        objectIn.position, objectIn.velocity = physics.leapfrog(objectIn.acceleration, objectIn.velocity, objectIn.position)
        # NOTE: fine to update planet position as next planet calcs will already have that planet's force calculated by pair calc previously