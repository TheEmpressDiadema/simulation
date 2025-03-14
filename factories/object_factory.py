from abc import abstractmethod

from environment.cell import Cell
from factories.factory import Factory
from entities.concrete import Rock, Tree, Grass


class ObjectFactory(Factory):

    @abstractmethod
    def create_object(self, position):
        pass


class RockFactory(ObjectFactory):

    def create_object(self, position: Cell):
        return Rock(position)


class TreeFactory(ObjectFactory):

    def create_object(self, position: Cell):
        return Tree(position)

class GrassFactory(ObjectFactory):

    def create_object(self, position: Cell):
        return Grass(position)