from abc import abstractmethod

from simulation.map.map import Map
from simulation.map.coordinate import Coordinate
from simulation.entities.entity import Entity, Grass, Resource
from simulation.config.config import PREDATOR_ICON, HERBIVORE_ICON


class Creature(Entity):

    target_type: type[Resource]

    def __init__(self, hp: int, speed: int):
        self._hp = hp
        self._speed = speed

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int):
        self._hp = value

    @property
    def speed(self) -> int:
        return self._speed

    @abstractmethod
    def eat(self, target: Entity):
        pass

    def make_move(self, path: list[Coordinate], field: Map):
        prev_cell = None
        for cell in path:
            content = field[cell]
            if isinstance(content, self.target_type):
                self.eat(content)
                if content.eaten:
                    field.delete_entity(cell)
            if field[cell] is None:
                field[cell] = self
                field[prev_cell] = None
            prev_cell = cell


class Herbivore(Creature, Resource):

    icon: str = HERBIVORE_ICON
    target_type: type[Resource] = Grass

    def __init__(self, hp: int, speed: int):
        Creature.__init__(self, hp, speed)
        Resource.__init__(self)

    def eat(self, target: Entity):
        if isinstance(target, self.target_type):
            target.mark_eaten()


class Predator(Creature):

    icon: str = PREDATOR_ICON
    target_type: type[Resource] = Herbivore

    def __init__(self, hp: int, speed: int, damage: int):
        super().__init__(hp, speed)
        self._damage = damage

    def eat(self, target: Entity):
        if isinstance(target, self.target_type):
            target.hp = max(0, target.hp - self._damage)
            if target.hp == 0:
                target.mark_eaten()
