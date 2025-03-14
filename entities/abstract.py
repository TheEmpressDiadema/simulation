from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

from environment.cell import Cell


class Entity(ABC):

    icon: str
    spawn_rate: float

    def __init__(self, position: Cell):
        self._position = position

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, pos: Cell):
        self._position = pos


@runtime_checkable
class IConsumable(Protocol):

    @abstractmethod
    def get_lifestatus(self):
        pass

class Resource(Entity, IConsumable):

    def __init__(self, position: Cell):
        super().__init__(position)
        self._is_alive = True
    
    def change_status(self):
        self._is_alive = False
    
    def get_lifestatus(self):
        return self._is_alive


class StaticObject(Entity):

    pass


class Creature(Entity):

    target_type: type[IConsumable]

    def __init__(self, position: Cell, attributes):
        super().__init__(position)
        self._health_points = attributes.health_points
        self._move_speed = attributes.move_speed
    
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
    def eat(self, target: IConsumable):
        pass