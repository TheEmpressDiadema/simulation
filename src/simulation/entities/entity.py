from abc import ABC

from simulation.config.config import ROCK_ICON, TREE_ICON, GRASS_ICON


class Entity(ABC):

    icon: str


class Resource(Entity):

    def __init__(self):
        self._eaten = False

    @property
    def eaten(self) -> bool:
        return self._eaten

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
