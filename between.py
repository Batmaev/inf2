def getBetween(ar, t):
    pre, nex = search(ar, t)
    return interpolate(pre, nex, t)

def search(ar, t):
    pre = ar[0]
    if pre.t <= t:
        for cur in ar:
            if(cur.t > t):
                return (pre, cur)
            pre = cur
        #print(f"search(t): t = {t} слишком большое")
        return (ar[-2], ar[-1])
    print(f"search(t): t = {t} слишком маленькое")
    return (ar[0], ar[1])
    


import classes
def interpolate(pre, nex, t):
    def lin(v1, v2, t1, t2, t):
        return v1 + (v2 - v1) / (t2 - t1) * (t - t1)
    res = classes.PosAndTime()
    res.x = lin(pre.x, nex.x, pre.t, nex.t, t)
    res.x = lin(pre.y, nex.y, pre.t, nex.t, t)
    res.z = lin(pre.z, nex.z, pre.t, nex.t, t)
    res.t = t
    return res
