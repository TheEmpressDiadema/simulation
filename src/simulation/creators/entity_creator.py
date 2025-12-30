from abc import ABC, abstractmethod

from simulation.entities.creature import Predator, Herbivore
from simulation.entities.entity import Entity, Tree, Rock, Grass
from simulation.config.config import (
    PREDATOR_DAMAGE,
    PREDATOR_HP,
    PREDATOR_SPEED,
    HERBIVORE_HP,
    HERBIVORE_SPEED,
)


class Factory(ABC):

    @abstractmethod
    def create_entity(self):
        pass


class TreeFactory(Factory):

    def create_entity(self) -> Tree:
        return Tree()


class RockFactory(Factory):

    def create_entity(self) -> Rock:
        return Rock()


class GrassFactory(Factory):

    def create_entity(self) -> Grass:
        return Grass()


class PredatorFactory(Factory):

    def create_entity(self) -> Predator:
        return Predator(PREDATOR_HP, PREDATOR_SPEED, PREDATOR_DAMAGE)


class HerbivoreFactory(Factory):

    def create_entity(self) -> Herbivore:
        return Herbivore(HERBIVORE_HP, HERBIVORE_SPEED)


class EntityCreator:

    _factory_dict: dict[str, Factory] = {
        "Tree": TreeFactory(),
        "Rock": RockFactory(),
        "Grass": GrassFactory(),
        "Predator": PredatorFactory(),
        "Herbivore": HerbivoreFactory(),
    }

    def create_entity(self, entity_name: str) -> Entity:
        return self._factory_dict[entity_name].create_entity()
