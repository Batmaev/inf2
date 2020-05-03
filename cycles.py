import classes
from one_step import abstract_delta, next_guide_cosines

def simulate_one_particle(parameters, start_position, start_guide_cosines, time_limit):
    arr = []
    next_position = start_position
    ngc = start_guide_cosines

    while(next_position.t < time_limit):
        arr.append(next_position)
        ngc = next_guide_cosines(parameters, ngc)
        delta = abstract_delta(parameters, ngc)
        next_position = next_position.add(delta)

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



