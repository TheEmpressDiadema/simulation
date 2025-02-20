from typing import Optional
from abstract_entities import Entity
from utils.coordinate import Coordinate


class World:

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._world: dict[Coordinate, Entity] = {}

    def __setitem__(self, key: Coordinate, value: Entity):
        self._world[key] = value

    def __getitem__(self, key: Coordinate):
        return self._world[key]
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value: int):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value: int):
        self._height = value

    def _init_world(self):
        for y in self._height:
            for x in self._width:
                self._map[Coordinate(x,y)] = None