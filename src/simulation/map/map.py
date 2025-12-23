from typing import Optional

from simulation.entities.entity import Entity
from simulation.map.coordinate import Coordinate

class Map:

    def __init__(self, height: int, width: int):
        self._height: int = height
        self._width: int = width
        self._map: dict[Coordinate, Optional[Entity]] = dict()

    def __setitem__(self, key: Coordinate, value: Optional[Entity]):
        self._map[key] = value

    def __getitem__(self, key: Coordinate) -> Optional[Entity]:
        return self._map.get(key)
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
    def get_adjacents(self, cell: Coordinate) -> list[Coordinate]:
        return [
            Coordinate(cell.row + 1, cell.col),
            Coordinate(cell.row, cell.col + 1),
            Coordinate(cell.row, cell.col - 1),
            Coordinate(cell.row - 1, cell.col)
        ]
    
    def in_border(self, cell: Coordinate) -> bool:
        return 1 <= cell.row <= self._height and 1 <= cell.col <= self._width

    def get_free_cells(self) -> list[Coordinate]:
        return [cell for cell in self._map if self._map[cell] is None]
    
    def get_entity_cells(self) -> list[Coordinate]:
        return [cell for cell in self._map if isinstance(self._map[cell], Entity)]