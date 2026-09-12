from objects import *

class ObjectManager:
    objectList = [] # list of all physics objects being simulated
    nextID = 0

    def __init__(self):
        pass
    
    def addObject(self, objectIn):    #add an object to the simulation
        self.objectList.append(objectIn)
        self.nextID += 1

    def addObjects(self, objectListIn):
        for currentObject in objectListIn:
            self.addObject(currentObject)
    
    def removeObject(self, objectIn): #remove an object from the simulation
        for currentObject in self.objectList:
            if currentObject is objectIn:
                self.objectList.remove(objectIn)
                self.nextID -= 1
                break

    def findObject(self, IDIn):
        for currentObject in self.objectList:
            if currentObject.ID == IDIn:
                return currentObject

    def instantiateObject(self, typeIn, parametersTupleIn):
        if typeIn.lower() == "planet":
            return self.instantiatePlanet(*parametersTupleIn)
        else:
            raise ValueError(f"ObjectManager could not instantiate object of type {typeIn}")

    def instantiatePlanet(self, IDIn, positionIn, radiusIn, velocityIn, massIn, colourIn):
        return Planet(IDIn, positionIn, radiusIn, velocityIn, massIn, colourIn)

    def instantiatePlanets(self, planetParameterListIn):
        returnList = []
        for parameter in planetParameterListIn:
            returnList.append(self.instantiatePlanet(*parameter))

        return returnList