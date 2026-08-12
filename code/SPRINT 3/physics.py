# JUST standalone functions to be used by simulation.py - NO OBJECTS TO BE PASSED IN just values in and out

# in/out order:
# - force
# - acceleration
# - velocity
# - position
# - time
# - misc other e.g. mass
from vector import *

def addForce(forceDictIn):
    resultantForceOut = Vector(0,0)
    for item in forceDictIn:
        resultantForceOut += forceDictIn[item]
    return resultantForceOut


def calcAcceleration(forceIn, massIn):
    accelerationOut = forceIn / massIn
    return accelerationOut

def calcForce(r1, r2, m1, m2):
    deltar = (r2 - r1)
    deltarMagnitude = deltar.length()   # £££ pythagoras
    F = m1 * m2 * deltar / (deltarMagnitude)**3
    return F

def drift(v, r, h):
    rNew = r + (0.5 * h * v)
    return rNew

def kick(a, v, h):
    vNew = v + (a * h)
    return vNew