# NOTE: no actual maths happens here - that's what physics.py is for!
import physics

class Simulation:
    _objectList = [] # list of all physics objects being simulated
    _speed = 1.0     # the overall speed of the simulation
    _speedIncriment = 1.5    # the ammount the simulations speed is multiplied and divided by each button press
    _operations = 0  # the rolling number of .tick operations to do each frame
    _rewind = False  # true if the simulation is playing backwards
    _paused = False
    _simulationUses = "fixed"   # use "fixed" to have a fixed timestep each calculation (more orbitally accurate), use "dynamic" to use dt for h (more clock-accurate)

    def addObject(self, objectIn):    #add an object to the simulation
        self._objectList.append(objectIn)

    def removeObject(self, objectIn): #remove an object from the simulation
        for currentObject in self._objectList:
            if currentObject is objectIn:
                self._objectList.remove(objectIn)

    def findObject(self, IDIn):
        for currentObject in self._objectList:
            if currentObject.ID == IDIn:
                return currentObject


    # called each frame, has logic for pausing & simulation speed
    def frame(self, dt, framerate):
        if not self._paused: # if paused, doesn't run physics
            self._operations += self._speed
            while self._operations >= 1:   # if simulation speed = 2, it will run all of the physics twice per tick
                if self._simulationUses == "fixed":
                    self._tick(1/framerate)
                elif self._simulationUses == "dynamic":
                    self._tick(dt)
                else:
                    raise ValueError(f"Unrecognised simulation mode: {self._simulationUses}")
                self._operations -= 1


    # update all physics here
    def _tick(self, dt):
        # clear each planet's forceDict
        for currentObject in self._objectList:
            currentObject.forceDict = {}
        # main physics updating all object attributes
        for currentObject in self._objectList:
            self._leapfrog(currentObject, dt)    # update all attributes of the current planet using the leapfrog method
    

    # changing all physics-related variables for the object
    def _leapfrog(self, objectIn, dt):
        v = objectIn.velocity; r = objectIn.position; h = dt    # assign easier to understand var names
        rMid = physics.drift(v, r, h)
        a = self._updateAcceleration(objectIn, rMid) # calculate acceleration & forces on the planet (also assigns self.acceleration to the new value)
        vNew = physics.kick(a, v, h)
        rNew = physics.drift(vNew, rMid, h)
        objectIn.velocity = vNew; objectIn.position = rNew

    
    def _updateAcceleration(self, objectIn, positionIn):
        objectIn.position = positionIn  # set position to rMid
        self._updateForces(objectIn)     # update the force dictionary
        self._calcResultantForce(objectIn)   # add all the forces in the force dictionary
        objectIn.acceleration = physics.calcAcceleration(objectIn.resultantForce, objectIn.mass)  # calculate acceleration
        return objectIn.acceleration

    def _updateForces(self, objectIn):   # find each of the forces effecting THIS object
        for currentObject in self._objectList:   # loops through all planets in simulation
            if not currentObject is objectIn:   # makes sure it's not itself
                currentID = objectIn.ID   # finds the ID of THIS object
                targetID = currentObject.ID   # finds the ID of the OTHER object
                if not targetID in objectIn.forceDict.keys():    # makes sure it hasn't already been calculated
                    pullForce = self._calcPull(objectIn, currentObject)      # EXPENSIVE: calculates the vector force pull between THIS and the OTHER
                    objectIn.forceDict[targetID] = pullForce        # assigns THIS object's planetID to be the calculated vector force in its forceDict
                    currentObject.forceDict[currentID] = -pullForce # assigns the OTHER object's planetID to be the negative of the calculated vector force in its forceDict
                # else the force pair was already calculated by a previous object
                
    def _calcPull(self, object1, object2):
        force = physics.calcForce(object1.position, object2.position, object1.mass, object2.mass)
        return force
    
    def _calcResultantForce(self, objectIn):
        objectIn.resultantForce = physics.addForce(objectIn.forceDict)


    def selectionDetection(self, mousePosition, UI):
        currentSelected = False
        found = False
        for currentObject in self.objectList:
            currentSelected = currentObject.selectionDetection(mousePosition, UI)
            if currentSelected:
                found = True
                
        if not found:
            UI.disselect()

    def pauseToggle(self):
        self._paused = not self._paused

    def pause(self):
        if not self._paused:
            self._paused = True

    def play(self):
        if self._paused:
            self._paused = False

    def reverse(self):  # for rewinding the simulation
        for currentObject in self._objectList:
            currentObject.velocity *= -1
        # toggles the rewind bool attribute
        self._rewind = not self._rewind

    def speedUp(self):
        self._speed *= self._speedIncriment

    def speedDown(self):
        self._speed /= self._speedIncriment

    @property
    def objectList(self):
        return self._objectList

    @property
    def paused(self):
        return self._paused