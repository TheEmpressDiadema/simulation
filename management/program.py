from time import sleep
from threading import Event, Thread

from management.menu import Menu
from constants.states import Commands
from constants.world_size import WorldSize
from management.renderer import Renderer
from management.simulation import Simulation


class Program:

    def __init__(self):
        self._world_params = WorldSize()
        self._simulation = Simulation(self._world_params)
        self._renderer = Renderer()
        self._menu = Menu()

    def run(self):
        run_event = Event()
        stop_event = Event()

        subthread = Thread(target=self._run_simulation, 
                           args=(run_event, stop_event), daemon=True)

        subthread.start()

        self._run_menu(run_event, stop_event)
    
    def _run_menu(self, run_event: Event, stop_event: Event):

        self._renderer.print_menu(self._menu)

        while True:

            comma = input().strip().lower()

            match comma:
                case Commands.START.value:
                    run_event.set()
                case Commands.PAUSE.value:
                    run_event.clear()
                    self._renderer.print_menu(self._menu)
                case Commands.QUIT.value:
                    stop_event.set()
                    break
                case _:
                    continue

    def _run_simulation(self, run_event: Event, stop_event: Event):
        self._simulation.start_simulation()

        while not (stop_event.is_set() or self._simulation.world.is_full()):
            if run_event.is_set():
                self._renderer.render(self._simulation.world)

                self._simulation.next_turn()
                sleep(1)