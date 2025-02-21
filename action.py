from abc import ABC, abstractmethod

class Action(ABC):

    @abstractmethod
    def execute(self):
        pass


class SpawnEntity(Action):

    def execute(self):
        pass


class RemoveEntities(Action):

    def execute(self):
        pass