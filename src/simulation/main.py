from simulation.algorithms.path_builder import BFS, RandomPathBuilder
from simulation.actions.action import MoveEntities
from simulation.entities.creatures import Herbivore, Predator
from simulation.map.coordinate import Coordinate
from simulation.map.map import Map
from simulation.view.renderer import Renderer
from simulation.config.config import *

def main() -> None:
    field = Map(MAP_HEIGHT, MAP_WIDTH)
    renderer = Renderer()
    renderer.print_field(field)
    print()
    p1 = Predator(Coordinate(1,1), PREDATOR_HP, PREDATOR_SPEED, PREDATOR_DAMAGE)
    field[Coordinate(1,1)] = p1
    renderer.print_field(field)
    p2 = Herbivore(Coordinate(2,2), HERBIVORE_HP, HERBIVORE_SPEED)
    field[Coordinate(2,2)] = p2
    print()
    renderer.print_field(field)
    print()
    act = MoveEntities()
    act.run(field)
    renderer.print_field(field)
    print()
    print(p2.hp)