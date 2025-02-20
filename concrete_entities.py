from utils.coordinate import Coordinate
from abstract_entities import (
    IConsumable, StaticObject,
    Resource, Creature
)
from config import (
    ROCK_ICON, TREE_ICON, GRASS_ICON,
    PREDATOR_ICON, HERBIVORE_ICON
)


class Rock(StaticObject):

    icon: str = ROCK_ICON


class Tree(StaticObject):

    icon: str = TREE_ICON


class Grass(Resource):

    icon: str = GRASS_ICON


class Herbivore(Creature, IConsumable):

    icon: str = HERBIVORE_ICON
    target_type: type[Resource] = Grass

    def get_status(self):
        return self._health_points > 0
    
    def eat(self, target: Resource):
        if isinstance(target, self.target_type):
            target.change_status()


class Predator(Creature):

    icon: str = PREDATOR_ICON
    target_type: type[IConsumable] = Herbivore

    def __init__(self, position: Coordinate, health_points: int, 
                 move_speed: int, damage: int):
        super().__init__(position, health_points, move_speed)
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    def eat(self, target: IConsumable):
        if isinstance(target, self.target_type):
            target.health_points = max(target.health_points - self._damage, 0)