import time

from actions.spawn import SpawnEntity
from actions.move import MoveCreatures
from management.renderer import Renderer
from environment.world import World


world = World(10, 10)
renderer = Renderer()
while True:
    spawn_entity = SpawnEntity()
    move_action = MoveCreatures()
    spawn_entity.execute(world)
    print("Spawned new Entity!")
    renderer.render(world)
    time.sleep(1)
    move_action.execute(world)
    print("Entities Moved")
    renderer.render(world)
    time.sleep(1)