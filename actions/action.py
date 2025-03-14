from abc import ABC, abstractmethod

from environment.world import World


class Action(ABC):

    @abstractmethod
    def execute(self, world: World):
        pass