from environment.cell import Cell
from entities.abstract import Entity

class World:

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._content: dict[Cell, Entity] = dict()

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def is_full(self):
        return len(self.get_free_cells()) == 0

    def in_border(self, cell: Cell):
        in_border_flag = (0 <= cell.col < self._width)
        in_border_flag &= (0 <= cell.row < self._height)
        return in_border_flag

    def set_entity(self, cell: Cell, entity: Entity):
        self._content[cell] = entity

    def remove_entity(self, cell: Cell):
        if cell in self._content.keys():
            self._content.pop(cell)

    def get_cell_content(self, cell: Cell) -> Entity | None:
        return self._content.get(cell)
    
    def get_entities(self) -> list[Entity]:
        return list(self._content.values())

    def replace_entity(self, cell_from: Cell, cell_to: Cell):
        self._content[cell_to] = self._content[cell_from]
        if cell_to != cell_from:
            self.remove_entity(cell_from)

    def get_free_cells(self) -> list[Cell]:
        free_cells: list[Cell] = list()

        for col in range(self._width):
            for row in range(self._height):
                cell = Cell(col, row)
                if self._content.get(cell) is None:
                    free_cells.append(cell)
        
        return free_cells