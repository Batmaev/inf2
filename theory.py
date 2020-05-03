# В этом файле - аналитические решения

D = 0

def setParameters(parameters):
    global D 
    D = 1/3 * parameters.lmbda * parameters.velocity

def distance(t):
    return (6 * D * t)**0.5