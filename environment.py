from typing import Optional
from abstract_entities import Entity


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


class Map:

    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height
        self._map: dict[Coordinate, Entity] = {}

    def __getitem__(self, key: Coordinate):
        return self._map[key]

    def __setitem__(self, key: Coordinate, value: Optional[Entity]):
        self._map[key] = value

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
