import random

from typing import Protocol
from abc import abstractmethod

from environment.cell import Cell
from environment.world import World
from constants.directions import DIRECTIONS
from entities.abstract import Creature, Entity

class PathBuilder(Protocol):

    @abstractmethod
    def build_path(self, creature: Creature, world: World):
        pass


class BFS(PathBuilder):

    def build_path(self, creature: Creature, world: World):
        
        queue: set[Cell] = set()
        used: dict[Cell, bool] = dict()
        path: dict[Cell, Cell] = dict()

        start = creature.position
        img_cell = Cell(-1, -1)
        target_cell = start

        queue.add(start)
        used[start] = True
        path[start] = img_cell

        while len(queue) > 0:

            cell_from = queue.pop()
            target_found = False

            for direction in DIRECTIONS:

                cell_to = Cell(cell_from.col + direction[0], cell_from.row + direction[1])

                if used.get(cell_to) is None and world.in_border(cell_to):

                    used[cell_to] = True
                    path[cell_to] = cell_from
                    content = world.get_cell_content(cell_to)

                    if isinstance(content, creature.target_type):
                        
                        target_found = True
                        target_cell = cell_to
                        break

                    if content is None:

                        queue.add(cell_to)
                
            if target_found:
                break
        
        result_path = []

        while path[target_cell] != img_cell:

            result_path.append(target_cell)
            target_cell = path[target_cell]
        
        result_path.reverse()
        return result_path
                    

class RandomBuilder(PathBuilder):

    def build_path(self, creature: Creature, world: World):
        
        cell_from = creature.position
        move_count = creature.move_speed
        path = []

        while move_count > 0:

            used = set()
            directions = DIRECTIONS.copy()

            for direction in directions:

                cell_to = Cell(cell_from.col + direction[0], cell_from.row + direction[1])
                content = world.get_cell_content(cell_to)

                if isinstance(content, Entity) or not world.in_border(cell_to):

                    used.add(direction)
            
            directions = list(set(directions) - used)
            
            if len(directions) == 0:
                break
            
            random_direction = random.choice(directions)
            cell_to = Cell(cell_from.col + random_direction[0], cell_from.row + random_direction[1])
            cell_from = cell_to
            path.append(cell_to)

            move_count -= 1

        return path