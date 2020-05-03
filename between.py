# В этом файле - функция getBetween, которая позволяет 
# получить координаты в произвольный момент времени. 
# В массиве, который выдаёт cycles.simulate_one_particle,
# есть только узловые точки - те, в которых направление 
# скорости изменилось в результате столкновения 

def getBetween(ar, t):
    pre, nex = search(ar, t)
    return interpolate(pre, nex, t)

def search(ar, t):
    #Идея в том, что если вызываю эту функцию на одном массиве снова 
    # и снова, то не обязательно начинать перебирать с начала
    i = 0

    if ar == search.prevArray:
        if ar[search.prevResult].t <= t:
            i = search.prevResult
    else:
        search.prevArray = ar

    pre = ar[i]

    if pre.t <= t:
        for j in range(i, len(ar)):
            cur = ar[j]
            if(cur.t > t):
                search.prevResult = j - 1
                return (pre, cur)
            pre = cur
        print(f"search(t): t = {t} слишком большое")
        return (ar[-2], ar[-1])
    print(f"search(t): t = {t} слишком маленькое")
    return (ar[0], ar[1])

search.prevArray = False
search.prevResult = 0
    


from classes import PosAndTime
def interpolate(pre, nex, t):
    def lin(v1, v2, t1, t2, t):
        return v1 + (v2 - v1) / (t2 - t1) * (t - t1)
    res = PosAndTime()
    res.x = lin(pre.x, nex.x, pre.t, nex.t, t)
    res.y = lin(pre.y, nex.y, pre.t, nex.t, t)
    res.z = lin(pre.z, nex.z, pre.t, nex.t, t)
    res.t = t
    return res
