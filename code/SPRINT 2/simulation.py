# update all the physics when simulation.tick() called
# mainly object management and controlling what physics functions are called
# NOTE: no actual maths happens here - that's what physics.py is for!
import pygame
import physics

class Simulation:
    objectList = []

    def addObject(self, objectIn):    #add an object to the simulation
        self.objectList.append(objectIn)

    def removeObject(self): #remove an object from the simulation
        pass

    def tick(self, dt):
        # clear each planet's forceList
        for currentObject in self.objectList:
            currentObject.forceList = []    # wipes forceList
            for i in range(len(self.objectList)-1):
                currentObject.forceList.append(pygame.Vector2(0,0)) # adds a (0,0) slot for each other planet in forceList
            print(f"currentObject at {currentObject.position} has this forceList: {currentObject.forceList}")

        # main physics updating all object attributes
        for currentObject in self.objectList:
            self.findForces(currentObject)  # find all forces acting on the object
            self.addForces(currentObject)   # add all the forces together
            self.leapfrog(currentObject, dt)    # find acceleration and velocity, and update position


    def findForces(self, objectIn):   # find each of the forces effecting current object
        pass    # find force pairs and update both planets force

    def addForces(self, objectIn):
        objectIn.resultantForce = physics.resultantForce(objectIn.forceList)

    def leapfrog(self, objectIn, dt):
        objectIn.acceleration, objectIn.velocity, objectIn.position = physics.leapfrog(objectIn.resultantForce, objectIn.velocity, objectIn.position, dt, objectIn.mass)