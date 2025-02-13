import config

from typing import Type
from abc import ABC, abstractmethod


class Entity(ABC):

    icon: str
    spawn_probability: float


class StaticObject(ABC):

    spawn_probability: float = config.STATIC_OBJECT_PROBABILITY


class Resource(ABC):

    spawn_probability: float = config.RESOURCE_PROBABILITY


class Creature(ABC):

    target_type: Type[Entity]
    spawn_probability: float = config.CREATURE_PROBABILITY

    def __init__(self, health_points: int, move_speed: int):
        self._health_points = health_points
        self._move_speed = move_speed

    @property
    def health_points(self):
        return self._health_points
    
    @property
    def move_speed(self):
        return self._move_speed

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self, target: Entity):
        pass