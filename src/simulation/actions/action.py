from abc import ABC, abstractmethod
from random import choice as choose_cell

from simulation.entities.entity import Entity
from simulation.map.coordinate import Coordinate
from simulation.map.map import Map
from simulation.entities.creature import Creature
from simulation.creators.entity_creator import EntityCreator
from simulation.algorithms.path_builder import BFS, RandomPathBuilder
from simulation.config.config import MAX_ENTITY_COUNT


class Action(ABC):

    @abstractmethod
    def run(self):
        pass


class SpawnEntity(Action):

    def __init__(self):
        self._entity_creator = EntityCreator()

    def run(self, field: Map):
        for classname, max_count in MAX_ENTITY_COUNT.items():
            count_diff = max_count - field.get_entity_count(classname)
            for _ in range(count_diff):
                free_cells: list[Coordinate] = field.get_free_cells()
                if len(free_cells) > 0:
                    free_cell: Coordinate = choose_cell(free_cells)
                    entity = self._entity_creator.create_entity(classname)
                    field[free_cell] = entity


class MoveCreature(Action):

    def __init__(self):
        self._path_builder: BFS = BFS()
        self._random_builder: RandomPathBuilder = RandomPathBuilder()

    def run(self, field: Map):
        entity_cells: list[Coordinate] = field.get_entity_cells()
        existing_types: list[type[Entity]] = field.get_existing_types()
        for cell in entity_cells:
            if isinstance(field[cell], Creature):
                self._move_creature(cell, existing_types, field)

    def _move_creature(
        self, creature_cell: Coordinate, existing_types: list[type[Entity]], field: Map
    ):
        creature: Creature = field[creature_cell]
        if creature.target_type in existing_types:
            path = self._path_builder.build_path(creature_cell, field)
        else:
            path = self._random_builder.build_path(creature_cell, field)
        creature.make_move(path, field)
