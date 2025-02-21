import random

from world import World
from config import MOVE_DIRECTIONS
from abc import abstractmethod, ABC
from abstract_entities import Creature
from utils.coordinate import Coordinate


class PathBuilder(ABC):

    @abstractmethod
    def build_path(self, creature: Creature, world: World) -> list[Coordinate]:
        pass

    def _in_border(self, cell: Coordinate, world: World):
        in_border = cell.x in range(world.width)
        in_border &= cell.y in range(world.height)
        return in_border


class BFS(PathBuilder):

    def build_path(self, creature: Creature, world: World) -> list[Coordinate]:

        queue: set[Coordinate] = set()
        used: dict[Coordinate, bool] = dict()
        path: dict[Coordinate, Coordinate] = dict()

        start = creature.position
        img_coordinate = Coordinate(-1, -1)
        target_cell = Coordinate(-1, -1)

        queue.add(start)
        used[start] = True
        path[start] = img_coordinate

        while len(queue) > 0:

            cell_from = queue.pop()
            target_found = False

            for direction in MOVE_DIRECTIONS:

                cell_to = Coordinate(cell_from.x + direction[0], cell_from.y + direction[1])

                if self._in_border(cell_to, world):

                    used[cell_to] = True
                    path[cell_to] = cell_from.copy()

                    if isinstance(world[cell_to], creature.target_type):

                        target_found = True
                        target_cell = cell_to.copy()
                        break

                    if world[cell_to] is None:

                        queue.add(cell_to)
            
            if target_found:
                break

        result_path = []

        while path[target_cell] != img_coordinate:

            result_path.append(target_cell)
            target_cell = path[target_cell].copy()

        result_path.reverse()

        return result_path
    

class RandomPathBuilder(PathBuilder):

    def build_path(self, creature: Creature, world: World) -> list[Coordinate]:
        
        cell_from = creature.position.copy()
        move_count = creature.move_speed
        path = []

        while move_count:

            directions = MOVE_DIRECTIONS.copy()
            used = set()

            for direction in MOVE_DIRECTIONS:

                cell_to = Coordinate(cell_from.x + direction[0], cell_from.y + direction[1])

                if not self._in_border(cell_to, world) or world[cell_to] is not None:

                    used.add(direction)
            
            directions = list(set(directions) - used)

            if len(directions) == 0:
                break

            random_direction = random.choice(directions)
            cell_to = Coordinate(cell_from.x + random_direction[0], cell_from.y + random_direction[1])
            cell_from = cell_to.copy()
            path.append(cell_to)

            move_count -= 1
        
        return path