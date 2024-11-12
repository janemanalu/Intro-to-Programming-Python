import math
import stdio


# An immutable data type to represent a circle in 2D space.
class Circle:
    def __init__(self, x=0, y=0, r=1):
        self._x = x
        self._y = y
        self._r = r
    def distTo(self, other):
        return math.sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

    def clone(self):
        return Circle(self._x, self._y, self._r)

    def __abs__(self):
        return math.pi * (self._r ** 2)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ", " + str(self._r) + ")"


# Unit tests the data type.
def _main():
    c1 = Circle(3, 4)
    c2 = Circle()
    stdio.writeln(c1)
    stdio.writeln(c2)
    stdio.writeln(c1.distTo(c2))
    stdio.writeln(c1.clone())
    stdio.writeln(abs(c1))
    stdio.writeln(c1 < c2)
    stdio.writeln(c1 == c2)


if __name__ == "__main__":
    _main()
