class Cell:

    def __init__(self, col: int, row: int):
        self._col = col
        self._row = row

    def __hash__(self):
        return hash((self._col, self._row))
    
    def __eq__(self, other):
        if isinstance(other, Cell):
            return self._col == other.col and self._row == other.row
        return False
    
    @property
    def col(self):
        return self._col
    
    @property
    def row(self):
        return self._row