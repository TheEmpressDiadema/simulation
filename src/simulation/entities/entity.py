from abc import ABC, abstractmethod
from typing import Protocol


class Entity(ABC):

    icon: str

class Food(Protocol):
    pass

class Resource(Entity):
    pass

class StaticObject(Entity):
    pass

class Creature(Entity):
    
    def __init__(self):
        super().__init__()