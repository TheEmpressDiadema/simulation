import random

from actions.action import Action
from environment.world import World
from entities.abstract import Entity
from config.attributes import (
    CreatureAttributes, HerbivoreAttributes,
    PredatorAttributes
)
from factories.object_factory import (
    RockFactory, GrassFactory, 
    TreeFactory
)
from factories.creature_factory import (
    PredatorFactory,
    HerbivoreFactory
)
from factories.factory import Factory
from entities.concrete import (
    Rock, Tree, Grass,
    Herbivore, Predator
)


class SpawnEntity(Action):

    def __init__(self):
        self._class_factories: dict[type[Entity], Factory] = {
            Rock : RockFactory(), 
            Tree : TreeFactory(), 
            Grass : GrassFactory(), 
            Herbivore : HerbivoreFactory(), 
            Predator : PredatorFactory()
            }
        self._class_attributes: dict[type[Entity], CreatureAttributes] = {
            Herbivore : HerbivoreAttributes(), 
            Predator : PredatorAttributes()
        }
    
    def execute(self, world: World):
        free_cells = world.get_free_cells()

        if len(free_cells) == 0:
            return
        
        free_cell = random.choice(free_cells)
        entity_class = self._choose_entity_class()
        attributes = self._class_attributes.get(entity_class)

        if attributes is None:
            entity = self._class_factories[entity_class].create_object(free_cell)
        else:
            entity = self._class_factories[entity_class].create_creature(free_cell, attributes)
        
        world.set_entity(free_cell, entity)
    
    def _choose_entity_class(self) -> type[Entity]:
        random_value = random.uniform(0, 1)
        rate = 0.0
        result_class = None

        for entity_class in self._class_factories.keys():
            rate += entity_class.spawn_rate

            if random_value <= rate:
                result_class = entity_class
                break
        
        return result_class