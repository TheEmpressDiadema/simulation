from abc import abstractmethod

from environment.cell import Cell
from factories.factory import Factory
from entities.concrete import Herbivore, Predator
from config.attributes import (
    CreatureAttributes, HerbivoreAttributes,
    PredatorAttributes
)


class CreatureFactory(Factory):

    @abstractmethod
    def create_creature(self, position: Cell, attributes: CreatureAttributes):
        pass


class HerbivoreFactory(CreatureFactory):

    def create_creature(self, position: Cell, attributes: HerbivoreAttributes):
        return Herbivore(position, attributes)


class PredatorFactory(CreatureFactory):

    def create_creature(self, position: Cell, attributes: PredatorAttributes):
        return Predator(position, attributes)