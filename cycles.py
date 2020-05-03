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

from between import getBetween
def meanDistance(arar, time_limit): #Возвращает массив t и массив средних distances
    Nsteps = 500
    Nparticles = len(arar)
    dt = time_limit / Nsteps

    tar = list(map(lambda n : n * dt, range(Nsteps)))
    dars = []
    for ar in arar:
        dars.append(list(map(lambda t : getBetween(ar, t).distance(), tar)))
    
    mar = []
    for i in range(Nsteps):
        mar.append(0)
        for dar in dars:
            mar[i] += dar[i] / Nparticles
    return (tar, mar)

import numpy
from math import fabs
def xyDistribution(arar, t):
    #print(arar[2][2].x)
    ra = list(map(lambda ar : getBetween(ar, t), arar))
    #print(len(ra))
    maxv = max(map(lambda obj : max(obj.x, obj.y), ra))
    minv = min(map(lambda obj : min(obj.x, obj.y), ra))
    #print(ra[1].x)
    #print(list(map(lambda obj : max(obj.x, obj.y), ra)))
    Ndots = 50
    cs = numpy.linspace(minv, maxv, Ndots)
    dx = dy = (cs[1] - cs[0]) / 2

    def countNear(x, y_filtered):
        return len(list(filter(lambda obj: fabs(obj.x - x) < dx, y_filtered)))
    def filterNear(y):
        return list(filter(lambda obj: fabs(obj.y - y) < dy, ra))

    #p = [[countNear(x, y) for x in cs] for y in cs]
    p = numpy.zeros((Ndots, Ndots))
    for y in range (Ndots):
        y_filtered = filterNear(cs[y])
        for x in range(Ndots):
            p[y][x] = countNear(cs[x], y_filtered)

    xss, yss = numpy.meshgrid(cs, cs)

    return (xss, yss, p)




