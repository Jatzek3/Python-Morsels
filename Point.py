class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'.format(self=self)

    def __str__(self):
        return f'The point has x={self.x}, y={self.y}, z={self.z} parameters'.format(self=self)

    def compare(self, self2):
        if self.x == self2.x and self.y == self2.y and self.z == self2.z:
            print("The points are equal")
        else:
            print("The points aren't equal")

    def __add__(self, other):
        return Point(self.x + other.x,self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)
