import time
import threading  

from simulation.map.map import Map   
from simulation.config.config import MAP_WIDTH, MAP_HEIGHT
from simulation.actions.action import MoveCreature, SpawnEntity
from simulation.view.menu import Menu
from simulation.view.renderer import Renderer

class Simulation:

    def __init__(self):
        self._move_counter = 0
        self._renderer = Renderer()
        self._menu_view = Menu()
        self._map = Map(MAP_HEIGHT, MAP_WIDTH)
        self._actions = [SpawnEntity(), MoveCreature()]
        self._stop_flag = False
        self._paused = False

    def run(self):
        input_thread = threading.Thread(target=self._input_listener, daemon=True)
        input_thread.start()

        self._menu_view.print_view()

        while not self._stop_flag:
            while self._paused and not self._stop_flag:
                time.sleep(0.1) 
            if self._stop_flag:
                break

            for action in self._actions:
                action.run(self._map)

            self._move_counter += 1
            self._renderer.print_field(self._map)

            time.sleep(1)

        print(f"Симуляция остановлена. Всего ходов: {self._move_counter}")

    def _input_listener(self):
        while not self._stop_flag:
            cmd = input().strip().lower()
            if cmd == 'q':
                self._stop_flag = True
                break
            elif cmd == 'p':
                self._paused = True
                print("Пауза. Введите 'c' для продолжения.")
            elif cmd == 'c':
                self._paused = False
                print("Продолжение.")



def main() -> None:
    Simulation().run()