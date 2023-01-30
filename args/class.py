class Square:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


sq = Square(100, 40)
#sq.width = 100
#sq.height = 40
ar = sq.area()
print(ar)


class Cube(Square):
    z = 0

    def __init__(self, width, height, z):
        Square.__init__(self, width, height)
        self.z = z

    def volume(self):
        return self.area() * self.z


c = Cube(100, 40, 5)
a = c.area()
v = c.volume()
print(a)