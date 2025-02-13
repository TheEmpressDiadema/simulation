from environment import Map
from abc import ABC, abstractmethod


class Action(ABC):

    @abstractmethod
    def execute(self, map: Map):
        pass


class InitMap(Action):
    
    pass


class SpawnEntity(Action):

    pass


class RemoveEntitiy(Action):

    pass