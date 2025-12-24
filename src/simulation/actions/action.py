from abc import ABC, abstractmethod

from simulation.entities.entity import Entity
from simulation.map.map import Map
from simulation.entities.creatures import Creature
from simulation.algorithms.path_builder import BFS, RandomPathBuilder


class Action(ABC):

    @abstractmethod
    def run(self):
        pass

class SpawnEntity(Action):

    def __init__(self):
        pass

    def run(self, field: Map):
        pass

class MoveCreature(Action):

    def __init__(self):
        self._path_builder: BFS = BFS()
        self._random_builder: RandomPathBuilder = RandomPathBuilder()

    def run(self, field: Map):
        entities: list[Entity] = field.get_entity_cells()
        existing_types: list[type[Entity]] = field.get_existing_types()
        for cell in entities:
            entity = field[cell]
            if isinstance(entity, Creature):
                self._move_creature(entity, existing_types, field)

    def _move_creature(self, creature: Creature, existing_types: list[type[Entity]], field: Map):
        if creature.target_type in existing_types:
            path = self._path_builder.build_path(creature, field)
        else:
            path = self._random_builder.build_path(creature, field)
        field[creature.position] = None
        creature.make_move(path, field)
        field[creature.position] = creature