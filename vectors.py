from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" %(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    
    def __bool__(self):
        return self.x or self.y

v1 = Vector(4, 4)
v2 = Vector(5, 3)
print(v1 + v2)

print(v1 * 3)

print(abs(v1))
print(bool(v1))
print(v1)