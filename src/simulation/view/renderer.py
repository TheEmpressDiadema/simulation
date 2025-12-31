import os


from simulation.config.config import FREE_CELL_ICON
from simulation.map.coordinate import Coordinate
from simulation.map.map import Map


class Renderer:

    def print_field(self, game_map: Map):
        self._clear_console()

        for row in range(1, game_map.height+1):
            for col in range(1, game_map.width+1):
                self._print_cell(game_map, Coordinate(row, col))
            print()
    
    def _print_cell(self, game_map: Map, coordinate: Coordinate):
        value = game_map[coordinate]
        if value is None:
            print(FREE_CELL_ICON, end='')
        else:
            print(game_map[coordinate].icon, end='')
    
    def _clear_console(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")