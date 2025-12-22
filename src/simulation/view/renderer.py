from simulation.config.config import FREE_CELL_ICON
from simulation.map.coordinate import Coordinate
from simulation.map.map import Map


class Renderer:

    def print_field(self, game_map: Map):
        
        for row in range(game_map.height):
            for col in range(game_map.width):
                self._print_cell(game_map, Coordinate(row, col))
            print()
    
    def _print_cell(self, game_map: Map, coordinate: Coordinate):
        value = game_map[coordinate]
        if value is None:
            print(FREE_CELL_ICON, end='')
        else:
            print(game_map[coordinate].icon, end='')