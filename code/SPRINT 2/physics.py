# JUST standalone functions to be used by simulation.py - NO OBJECTS TO BE PASSED IN just values in and out

# in/out order:
# - force
# - acceleration
# - velocity
# - position
# - misc other e.g. mass


def resultantForce(forceListIn):
    pass    # add forces
    #return resultantForceOut

def acceleration(forceIn, massIn):
    pass    # F=ma
    #return accelerationOut

def leapfrog(accelerationIn, velocityIn, positionIn):
    pass    #leapfrog
    #return newVelocity, newPosition