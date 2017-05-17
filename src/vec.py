from math import sqrt


class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
       return Vec(self.x * other, self.y * other)

    # Allow for commutative multiplication
    __rmul__ = __mul__

    def abs(self): 
        return sqrt(self.x * self.x + self.y * self.y)

    def __str__(self):
        return "( %d, %d )" % ( self.x, self.y )
