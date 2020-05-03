# В этом файле - аналитические решения

D6 = 0

def setParameters(parameters):
    global D6 
    D6 = 2 * parameters.lmbda * parameters.velocity

def distance(t):
    return (D6 * t)**0.5