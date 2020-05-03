# В этом файле - функции, которые позволяют смоделировать одно столкновение

import math
import random
import classes

def abstract_delta(parameters, guide_cosines):
    l = random.expovariate(1/parameters.lmbda)
    #l = - parameters.lmbda * math.log(1 - random.random())
    gc = guide_cosines

    delta = classes.PosAndTime()
    delta.x = l * gc.a
    delta.y = l * gc.b
    delta.z = l * gc.c
    delta.t = l / parameters.velocity

    return delta


def next_guide_cosines(parameters, 
previous_guide_cosines):
    
    phi = 2 * math.pi * random.random()
    sinPhi = math.sin(phi)
    cosPhi = math.cos(phi)

    cosTeta = 1 - 2 * random.random()

    pgc = previous_guide_cosines
    if math.fabs(pgc.c) < 0.99 :
        
        uglyRoot = math.sqrt(
            (1 - cosTeta**2) /
            (1 - pgc.c**2))

        a = cosTeta * pgc.a - (pgc.b * sinPhi - pgc.a * pgc.c * cosPhi) * uglyRoot
        b = cosTeta * pgc.b + (pgc.a * sinPhi + pgc.b * pgc.c * cosPhi) * uglyRoot
        c = cosTeta * pgc.c - (1 - pgc.c**2) * cosPhi * uglyRoot

        ss = a**2 + b**2 + c**2
        if(math.fabs(ss - 1) > 0.05):
            print(pgc)
            print(f"cosTeta = {cosTeta}, phi = {phi}")
            print(f"next: a={a}, b={b}, c={c}")
            return False

    else:
        sinTeta = math.sqrt(1 - cosTeta**2) #по рисунку b Teta меняется от 0 до 2*пи
        a = sinTeta * cosPhi
        b = sinTeta * sinPhi
        c = cosTeta

    return classes.GuideCosines(a, b, c)

if __name__ == "__main__":
        s1 = classes.GuideCosines(0.5, 0.5, 0.705)
        while(True):
            s2 = s1
            s2 = next_guide_cosines(s1)
            ss = s2.a**2 + s2.b**2 + s2.c**2
            if(math.fabs(ss - 1) > 0.05):
                print(s1)
                print(s2)
                break