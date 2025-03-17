from actions.action import Action
from constants.world_size import WorldSize
from environment.world import World
from actions.spawn import SpawnEntity
from actions.move import MoveCreatures

class Simulation:

    def __init__(self, size: WorldSize):
        self._world = World(size.width, size.height)
        self._turn_actions: Action = [SpawnEntity(), MoveCreatures()]
    
    @property
    def world(self):
        return self._world

    def start_simulation(self):
        self.next_turn()

    def pause_simulation(self):
        pass

    def next_turn(self):
        for action in self._turn_actions:
            action.execute(self._world)