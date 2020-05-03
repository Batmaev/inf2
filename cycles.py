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
