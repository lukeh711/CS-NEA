# JUST standalone functions to be used by simulation.py - NO OBJECTS TO BE PASSED IN just values in and out

# in/out order:
# - force
# - acceleration
# - velocity
# - position
# - time
# - misc other e.g. mass
import pygame
from constants import *

def addForce(forceDictIn):
    resultantForceOut = pygame.Vector2(0,0)
    for item in forceDictIn:
        resultantForceOut += forceDictIn[item]
    return resultantForceOut


def calcAcceleration(forceIn, massIn):
    accelerationOut = forceIn / massIn
    return accelerationOut

def calcForce(r1, r2, m1, m2):
    F = G * m1 * m2 * (r2 - r1) / ()    # !!TODO: COMPLETE THIS LOGIC

def drift(v, r, h):
    pass

def kick(a, v, r):
    pass