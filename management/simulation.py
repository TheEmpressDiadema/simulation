import time

from actions.action import Action
from environment.world import World
from actions.spawn import SpawnEntity
from actions.move import MoveCreatures
from management.renderer import Renderer

class Simulation:

    def __init__(self):
        self._world = World()
        self._turn_actions: Action = [SpawnEntity(), MoveCreatures()]
        self._renderer = Renderer()
    
    def start_simulation(self):
        self.next_turn()

    def pause_simulation(self):
        pass

    def next_turn(self):
        for action in self._turn_actions:
            action.execute(self._world)
            self._renderer.render(self._world)
            time.sleep(0.8)