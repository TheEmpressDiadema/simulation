from simulation.algorithms.path_builder import BFS, RandomPathBuilder
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
    path_builder = BFS()
    path = path_builder.build_path(p1, field)
    field[p1.position] = None
    p1.make_move(path, field)
    field[p1.position] = p1
    renderer.print_field(field)
    print(p2.hp)
    random_builder = BFS()
    p2_path = random_builder.build_path(p2, field)
    print(p2_path)
    field[p2.position] = None
    p2.make_move(p2_path, field)
    field[p2.position] = p2
    renderer.print_field(field)

main()