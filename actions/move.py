from actions.action import Action
from environment.cell import Cell
from environment.world import World
from entities.abstract import Creature, Entity
from algorithms.path_builders import BFS, RandomBuilder


class MoveCreatures(Action):

    def __init__(self):
        self._bfs = BFS()
        self._random_builder = RandomBuilder()
    
    def execute(self, world: World):
        entities = world.get_entities()
        used: dict[Cell, bool] = dict()

        for entity in entities:

            cell = entity.position

            if isinstance(entity, Creature):
                if used.get(cell) is None:
                    path = self._bfs.build_path(entity, world)

                    if len(path) == 0:

                        path = self._random_builder.build_path(entity, world)
                    
                    self._move_creature(entity, path, world)
                    world.replace_entity(cell, entity.position)
                    used[entity.position] = True
    
    def _move_creature(self, creature: Creature, path: list[Cell], world: World):

        for cell_index in range(min(len(path), creature.move_speed)):

            cell = path[cell_index]
            cell_content = world.get_cell_content(cell)

            if isinstance(cell_content, creature.target_type):

                creature.eat(cell_content)

                if not cell_content.get_lifestatus():

                    world.remove_entity(cell)
                    creature.position = cell

                else:
                    break

            else:
                creature.position = cell