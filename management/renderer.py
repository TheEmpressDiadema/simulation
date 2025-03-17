import os
import platform

from management.menu import Menu
from environment.cell import Cell
from environment.world import World
from entities.abstract import Entity
from constants.icons import FREE_CELL_ICON


class Renderer:

    def print_menu(self, menu: Menu):

        for item in menu.items:
            print(item)

    def render(self, world: World):
        self._clear_console()

        for row in range(world.height):
            for col in range(world.width):
                cell = Cell(col, row)
                content = world.get_cell_content(cell)
                self._print_content(content)
            print()

    def _print_content(self, content: Entity | None):
        if isinstance(content, Entity):
            print(content.icon, end='')
        else:
            print(FREE_CELL_ICON, end='')
    
    def _clear_console(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")