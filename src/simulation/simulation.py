import time
import threading

from simulation.actions.action import Action
from simulation.view.menu import Menu

class Simulation:

    def __init__(self):
        self._actions: Action

    def _process_input(self, user_input: str) -> str:
        return user_input.lower().strip()

    def run(self):
        pass