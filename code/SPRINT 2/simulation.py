# update all the physics when simulation.tick() called
# controls all the movement of all the planets
# doesnt care abt camera or key presses
import physics

class Simulation:
    def __init__(self, objectListIn):
        self.objectList = objectListIn

    def tick(self):
        for simulationObject in self.objectList:
            physics.thingy()

    def objectForces(self):
        pass    # find each of the forces effecting current object


    # BASIC CALCS
    def resultantForce(self):
        pass    # calc the resultant force

    def velocity(self):
        pass

    def position(self):
        pass

    def addObject():
        pass





# for each planet:
#   findallforcesactingonobject()
#   findresultantforce()
#   move() - without effecting other object's calculations by changing old position .`.old & new pos
# 
# 
# 
# 
# 
# 
# 