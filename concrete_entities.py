import config

from typing import Type
from abstract_entities import (
    Resource, StaticObject,
    Creature, Entity
)

class Rock(StaticObject):

    icon: str = config.ROCK_ICON
    spawn_probability: float = config.ROCK_PROBABILITY


class Tree(StaticObject):

    icon: str = config.TREE_ICON
    spawn_probability: float = config.TREE_PROBABILITY


class Grass(Resource):

    icon: str = config.GRASS_ICON
    spawn_probability: float = config.GRASS_PROBABILITY


class Herbivore(Creature):

    icon: str = config.HERBIVORE_ICON
    target_type: Type[Entity] = Grass
    spawn_probability: float = config.HERBIVORE_PROBABILITY


class Predator(Creature):

    icon: str = config.PREDATOR_ICON
    target_type: Type[Entity] = Herbivore
    spawn_probability: float = config.PREDATOR_PROBABILITY

    def __init__(self, health_points: int, move_speed: int, damage: int):
        super().__init__(health_points, move_speed)
        self._damage = damage

    @property
    def damage(self):
        return self._damage
