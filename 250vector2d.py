from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # for a in (self.x, self.y):
        #     return (a) # yield working or return the generator
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        fmt = f"{class_name}({self.x}, {self.y})"
        print(fmt)
        print("{}({!r}, {!r})".format(class_name, *self))
        print("%s(%f, %f)" % (class_name, *self))
        return fmt

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        print(self, self.typecode, ord(self.typecode), bytes([ord(self.typecode)]), array(self.typecode, self))
        return (bytes([ord(self.typecode)])+ bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

v1 = Vector2d(3, 4)
print(v1, v1.x, v1.y)

a, b = v1
print(a, b)
v1_clone = eval(repr(v1))
print(v1_clone)
print(bytes(v1))
print(bool(v1))