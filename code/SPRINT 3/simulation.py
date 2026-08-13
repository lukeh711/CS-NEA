# NOTE: no actual maths happens here - that's what physics.py is for!
import physics

class Simulation:
    # list of all objects in the simulation space
    objectList = []

    def addObject(self, objectIn):    #add an object to the simulation
        self.objectList.append(objectIn)

    def removeObject(self, objectIn): #remove an object from the simulation
        for currentObject in self.objectList:
            if currentObject is objectIn:
                self.objectList.remove(objectIn)


    # update all physics here
    def tick(self, dt):
        # clear each planet's forceDict
        for currentObject in self.objectList:
            currentObject.forceDict = {}

        # main physics updating all object attributes
        for currentObject in self.objectList:
            self.leapfrog(currentObject, dt)    # update all attributes of the current planet using the leapfrog method
    

    # changing all physics-related variables for the object
    def leapfrog(self, objectIn, dt):
        v = objectIn.velocity; r = objectIn.position; h = dt    # assign easier to understand var names
        rMid = physics.drift(v, r, h)
        a = self.updateAcceleration(objectIn, rMid) # calculate acceleration & forces on the planet (also assigns self.acceleration to the new value)
        vNew = physics.kick(a, v, h)
        rNew = physics.drift(vNew, rMid, h)
        objectIn.velocity = vNew; objectIn.position = rNew

    
    def updateAcceleration(self, objectIn, positionIn):
        objectIn.position = positionIn  # set position to rMid
        self.updateForces(objectIn)     # update the force dictionary
        self.calcResultantForce(objectIn)   # add all the forces in the force dictionary
        objectIn.acceleration = physics.calcAcceleration(objectIn.resultantForce, objectIn.mass)  # calculate acceleration
        return objectIn.acceleration

    def updateForces(self, objectIn):   # find each of the forces effecting THIS object
        for currentObject in self.objectList:   # loops through all planets in simulation
            if not currentObject is objectIn:   # makes sure it's not itself
                currentID = objectIn.objectID   # finds the objectID of THIS object
                targetID = currentObject.objectID   # finds the objectID of the OTHER object
                if not targetID in objectIn.forceDict.keys():    # makes sure it hasn't already been calculated
                    pullForce = self.calcPull(objectIn, currentObject)      # EXPENSIVE: calculates the vector force pull between THIS and the OTHER
                    objectIn.forceDict[targetID] = pullForce        # assigns THIS object's planetID to be the calculated vector force in its forceDict
                    currentObject.forceDict[currentID] = -pullForce # assigns the OTHER object's planetID to be the negative of the calculated vector force in its forceDict
                # else the force pair was already calculated by a previous object
                
    def calcPull(self, object1, object2):
        force = physics.calcForce(object1.position, object2.position, object1.mass, object2.mass)
        return force
    
    def calcResultantForce(self, objectIn):
        objectIn.resultantForce = physics.addForce(objectIn.forceDict)


    def flipVelocities(self):
        for currentObject in self.objectList:
            currentObject.velocity *= -1