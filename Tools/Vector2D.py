import math

class Vector2D(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_length(self):
        x2y2sum = self.x * self.x + self.y * self.y
        return math.sqrt(x2y2sum)

    def __setlenth(self,value):
        length = self.get_length()
        self.x *= value/length
        self.y *= value/length

    def normalize(self):
        length = self.get_length()
        if length != 0:
            return self/length
        return Vector2D(self)

