import random

from typing import Optional
from abc import ABC, abstractmethod

from simulation.map.map import Map
from simulation.entities.entity import Creature
from simulation.map.coordinate import Coordinate

class PathBuilder(ABC):

    def _check_cell(self, used: dict[Coordinate, bool], cell: Coordinate, field: Map):
        return all([not used[cell], field[cell] is None, field.in_border(cell)])

    @abstractmethod
    def build_path(self, creature: Creature, field: Map):
        pass

class BFS(PathBuilder):
    
    def build_path(self, creature: Creature, field: Map) -> list[Coordinate]:
        
        queue: set[Coordinate] = set()
        used: dict[Coordinate, bool] = dict()
        parents: dict[Coordinate, Optional[Coordinate]] = dict()

        queue.add(creature.position)
        used[creature.position] = True

        target_cell: Coordinate = Coordinate(-1, -1)

        while len(queue) > 0:
            cell_from = queue.pop()
            if isinstance(field[cell_from], creature.target_type):
                target_cell = cell_from
                break
            for cell_to in field.get_adjacents(cell_from):
                if self._check_cell(used, cell_to, field):
                    queue.add(cell_to)
                    parents[cell_to] = cell_from
                    used[cell_to] = True
        
        path: list[Coordinate] = []

        while parents[target_cell] is not None:
            path.append(target_cell)
            target_cell = parents[target_cell]

        path.reverse()

        return path
    
class RandomPathBuilder(PathBuilder):

    def build_path(self, creature: Creature, field: Map) -> list[Coordinate]:
        path_length: int = creature.speed
        cell_from: Coordinate = creature.position
        used: dict[Coordinate, bool] = dict()
        path: list[Coordinate] = []
        
        while path_length:

            empty_cells = []

            for cell_to in field.get_adjacents(cell_from):
                if self._check_cell(used, cell_to, field):
                    empty_cells.append(cell_to)

            if len(empty_cells):
                random_cell = random.choice(empty_cells)
                used[random_cell] = True
                path.append(random_cell)
                cell_from = random_cell

            path_length -= 1
        
        return path