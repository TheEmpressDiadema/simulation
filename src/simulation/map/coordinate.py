from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:

    col: int
    row: int