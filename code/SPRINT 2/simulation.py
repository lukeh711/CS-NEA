# update all the physics when simulation.tick() called
# mainly object management and controlling what physics functions are called
# NOTE: no actual maths happens here - that's what physics.py is for!
# TODO: add kick and drift methods to physics.py
# naming:
# updateX - various pieces of code to update that var (using sub methods for maths)
# calcX - take in object and send & recieve data to & from physics.py to calculate a value

import pygame
import physics

class Simulation:
    objectList = []

    def addObject(self, objectIn):    #add an object to the simulation
        self.objectList.append(objectIn)

    def removeObject(self): #remove an object from the simulation
        pass

    def tick(self, dt):
        # clear each planet's forceDict
        for currentObject in self.objectList:
            currentObject.forceDict = {}
            print(f"currentObject ID {currentObject.objectID} at {currentObject.position} has this forceDict: {currentObject.forceDict}")

        # main physics updating all object attributes
        for currentObject in self.objectList:
            self.leapfrog(currentObject, dt)    # update all attributes of the current planet using the leapfrog method
            print(f"currentObject ID {currentObject.objectID} at {currentObject.position} NOW has this forceDict: {currentObject.forceDict}")


    # changing all physics-related variables for the object
    def leapfrog(self, objectIn, dt):
        a = objectIn.acceleration; v = objectIn.velocity; r = objectIn.position; h = dt # assign easier to understand var names

        rMid = r + (0.5 * h * v)        # Drift
        a = self.updateAcceleration(objectIn, rMid)   # Update a
        vNew = v + (a * h)           # Kick
        rNew = rMid + (0.5 * h * vNew)  # Drift
        objectIn.velocity = vNew; objectIn.position = rNew

    def updateAcceleration(self, objectIn, positionIn):
        objectIn.position = positionIn  # set position to rMjd
        self.updateForces(objectIn)    # update the force dictionary
        self.calcResultantForce(objectIn)   # add all the forces in the force dictionary
        objectIn.acceleration = physics.calcAcceleration(objectIn.resultantForce, objectIn.mass)  # calculate acceleration
        return objectIn.acceleration

    def updateForces(self, objectIn):   # find each of the forces effecting current object
        for currentObject in self.objectList: # loops through all planets in simulation
            if not currentObject is objectIn:   # makes sure it's not itself
                targetID = currentObject.objectID   # finds the objectID of the object it's currently looking at 
                if objectIn.forceDict[targetID] == pygame.Vector2(0, 0):    # makes sure it hasn't already been calculated
                    pullForce = self.calcPull(objectIn, currentObject)      # EXPENSIVE: calculates the vector force pull between each of them
                    objectIn.forceDict[targetID] = pullForce    # assigns that planetID to have that force applied to it
                # else the force pair was already calculated by a previous object
                
    def calcPull(self, object1, object2):
        force = physics.calcForce(object1.position, object2.position, object1.mass, object2.mass)
        return force
    
    def calcResultantForce(self, objectIn):
        objectIn.resultantForce = physics.addForce(objectIn.forceDict)