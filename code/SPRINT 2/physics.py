# JUST standalone functions to be used by simulation.py - NO OBJECTS TO BE PASSED IN just values in and out

# in/out order:
# - force
# - acceleration
# - velocity
# - position
# - time
# - misc other e.g. mass
import pygame


def resultantForce(forceListIn):
    resultantForceOut = pygame.Vector2(0,0)
    for force in forceListIn:
        output += force
    return resultantForceOut


def acceleration(forceIn, massIn):
    accelerationOut = forceIn / massIn
    return accelerationOut

def leapfrog(F, v, r, h, m):   # calculating acceleration, new velocity and new position
    rMid = r + (0.5 * h * v)
    a = acceleration(F, m)  # !!!!!!!TODO IMPORTANT!!!!! rewrite line to somehow tell it to do all of the force and everything calcs here
    vNew = v - (a * rMid)
    rNew = rMid + (0.5 * h * vNew)
    return (a, vNew, rNew)