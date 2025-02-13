import config

from typing import Protocol, Type
from abstract_entities import Entity
from environment import Map, Coordinate


class Algorithm(Protocol):

    def find_path(self):
        pass


class BFS(Algorithm):

    def find_path(self, start: Coordinate, target_type: Type[Entity], map: Map):

        queue: set[Coordinate] = set()
        used: dict[Coordinate, bool] = dict()
        path: dict[Coordinate, Coordinate] = dict()
        dist: dict[Coordinate, int] = dict()

        img_coordinate = Coordinate(-1, -1)
        end_coordinate = Coordinate(-1, -1)

        queue.add(start)
        used[start] = True
        dist[start] = 0
        path[start] = img_coordinate

        while len(queue):
            target_found = False

            cell_from = queue.pop()

            for direction in config.DIRECTIONS:

                cell_to = Coordinate(cell_from.x + direction[0], cell_from.y + direction[1])

                if self._in_border(map, cell_to):

                    dist[cell_to] = dist[cell_from] + 1
                    path[cell_to] = cell_from
                    used[cell_to] = True

                    if isinstance(map[cell_to], target_type):
                        target_found = True
                        end_coordinate = cell_to
                        break

                    if not cell_to:
                        queue.add(cell_to)

            if target_found:
                break

        result_path = []

        while path[end_coordinate] != img_coordinate:
            result_path.append(end_coordinate)
            end_coordinate = path[end_coordinate]

        result_path.reverse()

        return result_path

    def _in_border(self, map: Map, cell: Coordinate):
        in_borders = cell.x in range(0, map.width)
        in_borders &= cell.y in range(0, map.height)
        return in_borders
