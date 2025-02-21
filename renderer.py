import os
import platform

from world import World


class Renderer:

    def render(self, world: World):
        self._clear()

    def _clear(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")