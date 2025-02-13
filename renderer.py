import os
import config

from typing import Optional
from abstract_entities import Entity
from environment import Coordinate, Map


class Renderer:

    def render(self, map: Map):

        self._clear()

        for y in range(map.height):
            for x in range(map.width):
                coordinate = Coordinate(x, y)
                content = map[coordinate]
                self._print_cell(content)
            print()

    def _print_cell(self, content: Optional[Entity]):
        if isinstance(content, Entity):
            print(content.icon)
        else:
            print(config.EMPTY_CELL_ICON)

    def _clear(self):
        os.system("cls")