from abc import ABC, abstractmethod


class Factory(ABC):

    def __getitem__(self):
        return self