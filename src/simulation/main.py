from simulation.actions.action import MoveCreature
from simulation.entities.creature import Herbivore, Predator
from simulation.entities.entity import Grass
from simulation.map.coordinate import Coordinate
from simulation.map.map import Map
from simulation.view.renderer import Renderer
from simulation.config.config import *

def main() -> None:
    field = Map(MAP_HEIGHT, MAP_WIDTH)
    renderer = Renderer()
    renderer.print_field(field)
    print()
    p1 = Predator(PREDATOR_HP, PREDATOR_SPEED, PREDATOR_DAMAGE)
    field[Coordinate(1,1)] = p1
    renderer.print_field(field)
    p2 = Herbivore(HERBIVORE_HP, HERBIVORE_SPEED)
    field[Coordinate(2,2)] = p2
    p3 = Grass()
    field[Coordinate(3,3)] = p3
    renderer.print_field(field)
    move_action = MoveCreature()
    move_action.run(field)
    renderer.print_field(field)

main()