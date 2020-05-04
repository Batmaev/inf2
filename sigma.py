# Эти функции возвращают косинус тета для разных вариантов функции сечения рассеивания

import math
import random

def const():
    return 1 - 2 * random.random()

def halfcos():
    cosOfHalfsquared = (1 - random.random())**(2/3)
    return 2 * cosOfHalfsquared - 1

def halfsin():
    sinOfHalfsquared = (random.random())**(2/3)
    return 1 - 2 * sinOfHalfsquared
