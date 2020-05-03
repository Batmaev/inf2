class PosAndTime(object):
    x = 0
    y = 0
    z = 0
    t = 0
    def add(self, delta):
        newPosAndTime = PosAndTime()
        newPosAndTime.x = self.x + delta.x
        newPosAndTime.y = self.y + delta.y
        newPosAndTime.z = self.z + delta.z
        newPosAndTime.t = self.t + delta.t 
        return newPosAndTime
    def distance(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

from collections import namedtuple
GuideCosines = namedtuple("GuideCosines", "a b c")

class Empty(object): #Здесь будут храниться параметры, например, длина свободного пробега
    pass