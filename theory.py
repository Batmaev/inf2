# В этом файле - аналитические решения
import math
D = 0

def setParameters(parameters):
    global D 
    D = 1/3 * parameters.lmbda * parameters.velocity

def distance(t):
    return math.sqrt(6 * D * t)

import numpy
def probabilityDensity(cs, t):
    return numpy.array([
        [1 / (4 * math.pi * D * t) * math.exp(-(x**2 + y**2)/4/D/t) for x in cs]
         for y in cs])