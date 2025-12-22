from abc import ABC, abstractmethod

from simulation.config.config import (
    PREDATOR_ICON, HERBIVORE_ICON,
    ROCK_ICON, TREE_ICON, GRASS_ICON
)
from simulation.map.coordinate import Coordinate


class Entity(ABC):

    icon: str

    def __init__(self, position: Coordinate):
        self._position = position

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, cell: Coordinate):
        self._position = cell

class Resource(Entity):
    
    def __init__(self):
        self._eaten = False

    def mark_eaten(self):
        self._eaten = True

class StaticObject(Entity):
    pass

class Rock(StaticObject):
    
    icon: str = ROCK_ICON

class Tree(StaticObject):
    
    icon: str = TREE_ICON

class Grass(Resource):
    
    icon: str = GRASS_ICON

class Creature(Entity):
    
    target_type: type[Entity]

    def __init__(self, position: Coordinate, hp: int, speed: int):
        super().__init__(position)
        self._hp = hp
        self._speed = speed

    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, value: int):
        self._hp = value

    @property
    def speed(self) -> int:
        return self._speed

    @abstractmethod
    def make_move(self, path: list[Coordinate]):
        pass

    @abstractmethod
    def eat(self, target: Entity):
        pass

class Herbivore(Creature):
    
    icon: str = HERBIVORE_ICON
    target_type: type[Entity] = Grass

    def make_move(self, path: list[Coordinate]):
        pass

    def eat(self, target: Grass):
        target.mark_eaten(True)


class Predator(Creature):
    
    icon: str = PREDATOR_ICON
    target_type: type[Entity] = Herbivore

    def __init__(self, position: Coordinate, hp: int, speed: int, damage: int):
        super().__init__(position, hp, speed)
        self._damage = damage

    def make_move(self, path: list[Coordinate]):
        pass

    def eat(self, target: Herbivore):
        target.hp = max(0, target.hp - self._damage)