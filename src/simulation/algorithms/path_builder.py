import random

from typing import Optional
from abc import ABC, abstractmethod

from simulation.map.map import Map
from simulation.entities.creature import Creature
from simulation.map.coordinate import Coordinate


class PathBuilder(ABC):

    @abstractmethod
    def build_path(self, start: Coordinate, field: Map):
        pass


class BFS(PathBuilder):

    def build_path(self, start: Coordinate, field: Map) -> list[Coordinate]:

        queue: set[Coordinate] = set()
        used: dict[Coordinate, bool] = dict()
        parents: dict[Coordinate, Optional[Coordinate]] = dict()

        creature: Creature = field[start]
        queue.add(start)
        used[start] = True

        target_cell: Coordinate = Coordinate(-1, -1)
        target_found: bool = False

        while len(queue) > 0:
            cell_from = queue.pop()
            for cell_to in field.get_adjacents(cell_from):
                if not used.get(cell_to):
                    parents[cell_to] = cell_from
                    used[cell_to] = True
                    if field[cell_to] is None and field.in_border(cell_to):
                        queue.add(cell_to)
                    if isinstance(field[cell_to], creature.target_type):
                        target_cell = cell_to
                        target_found = True
                        break
            if target_found:
                break

        path: list[Coordinate] = []

        while parents.get(target_cell) is not None:
            path.append(target_cell)
            target_cell = parents[target_cell]

        path.append(start)
        path.reverse()

        return path


class RandomPathBuilder(PathBuilder):

    def build_path(self, start: Coordinate, field: Map) -> list[Coordinate]:
        creature: Creature = field[start]
        path_length: int = creature.speed
        cell_from: Coordinate = start
        path: list[Coordinate] = [start]

        while path_length:

            empty_cells = []

            for cell_to in field.get_adjacents(cell_from):
                if field[cell_to] is None and field.in_border(cell_to):
                    empty_cells.append(cell_to)

            if len(empty_cells):
                random_cell = random.choice(empty_cells)
                path.append(random_cell)
                cell_from = random_cell

            path_length -= 1

        return path
