class Point:
    def __init__(self, x, y):
        if x > y:
            raise RuntimeError('x must be smaller than y')
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not __eq__(self, other)

    def __str__(self):
        return "p(" + str(self.__x) + ", " + str(self.__y) + ")"

    __repr__ = __str__

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y