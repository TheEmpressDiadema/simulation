from typing import Protocol
from abc import ABC, abstractmethod

from utils.coordinate import Coordinate


class Entity(ABC):

    icon: str

    def __init__(self, position: Coordinate):
        self._position = position

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, coordinate: Coordinate):
        self._position = coordinate

class IConsumable(Protocol):

    @abstractmethod
    def get_status(self):
        pass

class StaticObject(Entity):

    pass

class Resource(Entity, IConsumable):

    def __init__(self, position):
        super().__init__(position)
        self._is_eaten = False

    def change_status(self):
        self._is_eaten = True

    def get_status(self):
        return self._is_eaten

class Creature(Entity):
    
    icon: str
    target_type: type[IConsumable]

    def __init__(self, position: Coordinate, health_points: int, move_speed: int):
        super().__init__(position)
        self._health_points = health_points
        self._move_speed = move_speed

    @property
    def health_points(self):
        return self._health_points
    
    @health_points.setter
    def health_points(self, value: int):
        self._health_points = value

    @property
    def move_speed(self):
        return self._move_speed
    
    @abstractmethod
    def eat(self, target: type[IConsumable]):
        pass

    @abstractmethod
    def move(self, path: list[Coordinate]):
        pass