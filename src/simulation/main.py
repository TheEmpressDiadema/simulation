import time
from simulation.entities.creature import Herbivore
from simulation.map.map import Map

from simulation.actions.action import SpawnEntity, MoveCreature
from simulation.view.renderer import Renderer
from simulation.config.config import MAP_HEIGHT, MAP_WIDTH

def main() -> None:
    field = Map(MAP_HEIGHT, MAP_WIDTH)
    spawn_action = SpawnEntity()
    move_action = MoveCreature()
    renderer = Renderer()
    while True:
        spawn_action.run(field)
        renderer.print_field(field)
        print("spawned")
        time.sleep(2)
        move_action.run(field)
        renderer.print_field(field)
        print("moved all")
        time.sleep(2)
main()