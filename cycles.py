# В этом файле функции с циклами, хех.
# Они собственно моделируют - получают массив точек 
# и обрабатывают его - считают среднее удаление от центра
from one_step import abstract_delta, next_guide_cosines

def simulate_one_particle(parameters, start_position, start_guide_cosines, time_limit):
    arr = [start_position]
    next_position = start_position
    ngc = start_guide_cosines

    while(next_position.t < time_limit):
        ngc = next_guide_cosines(parameters, ngc)
        delta = abstract_delta(parameters, ngc)
        next_position = next_position.add(delta)
        arr.append(next_position)

    return arr

def simulate_multiple_particles(parameters, Nparticles, start_position, start_guide_cosines, time_limit):
    arar = []
    for i in range(Nparticles):
        arar.append(simulate_one_particle(parameters, start_position, start_guide_cosines, time_limit))
    return arar

import numpy
from between import getBetween

def meanDistance(arar, time_limit): #Возвращает массив t и массив средних distances
    Nsteps = 50
    Nparticles = len(arar)

    tar = numpy.linspace(0, time_limit, Nsteps)

    dars = []
    for ar in arar:
        dars.append([getBetween(ar, t).distance() for t in tar])
    
    mar = []
    for i in range(Nsteps):
        mar.append(0)
        for dar in dars:
            mar[i] += dar[i] / Nparticles
    return (tar, mar)

from math import fabs

def xyDistribution(arar, t, Ndots):
    ra = [getBetween(ar, t) for ar in arar]

    maxv = max([max(obj.x, obj.y) for obj in ra])
    minv = min([min(obj.x, obj.y) for obj in ra])
    cs = numpy.linspace(minv, maxv, Ndots)
    dx = dy = (cs[1] - cs[0]) / 2

    def countNear(x, y_filtered):
        return len([obj for obj in y_filtered if fabs(obj.x - x) < dx])
    def filterNear(y):
        return [obj for obj in ra if fabs(obj.y - y) < dy]

    #p = [[countNear(x, y) for x in cs] for y in cs]
    p = numpy.zeros((Ndots, Ndots))
    for y in range (Ndots):
        y_filtered = filterNear(cs[y])
        for x in range(Ndots):
            p[y][x] = countNear(cs[x], y_filtered)

    return (cs, p)




