class Coordinate:

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self._x == other.x and self._y == other.y
        return False

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value: int):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value: int):
        self._y = value

    def copy(self):
        return Coordinate(self._x, self._y)