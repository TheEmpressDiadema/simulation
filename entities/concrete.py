from environment.cell import Cell
from entities.abstract import (
    StaticObject, Resource,
    Creature, IConsumable
)
from constants.icons import (
    ROCK_ICON, TREE_ICON, GRASS_ICON,
    PREDATOR_ICON, HERBIVORE_ICON
)
from constants.spawn_rates import (
    ROCK_SPAWN_RATE, TREE_SPAWN_RATE, GRASS_SPAWN_RATE,
    PREDATOR_SPAWN_RATE, HERBIVORE_SPAWN_RATE
)


class Rock(StaticObject):

    icon = ROCK_ICON
    spawn_rate = ROCK_SPAWN_RATE


class Tree(StaticObject):

    icon = TREE_ICON
    spawn_rate = TREE_SPAWN_RATE


class Grass(Resource):

    icon = GRASS_ICON
    spawn_rate = GRASS_SPAWN_RATE


class Herbivore(Creature, IConsumable):

    icon = HERBIVORE_ICON
    spawn_rate = HERBIVORE_SPAWN_RATE
    target_type = Grass

    def get_lifestatus(self):
        return self._health_points > 0
    
    def eat(self, target: Grass):
        target.change_status()


class Predator(Creature):

    icon = PREDATOR_ICON
    spawn_rate = PREDATOR_SPAWN_RATE
    target_type = Herbivore

    def __init__(self, position: Cell, attributes):
        super().__init__(position, attributes)
        self._damage = attributes.damage
    
    @property
    def damage(self):
        return self._damage
    
    def eat(self, target: Herbivore):
        target.health_points = max(target.health_points - self._damage, 0)