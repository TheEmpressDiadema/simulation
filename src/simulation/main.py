import sys
import time
import threading     

def run_game(event: threading.Event):
    while True:
        event.wait()
        print("Игра играется...")
        time.sleep(1)

def process_input(event: threading.Event):
    while True:
        cmd = input().strip().lower()
        if cmd == "p":
            event.clear()
            print("Игра на паузе")
        if cmd == "c":
            event.set()
            print("Игра продолжается")
        if cmd == "e":
            sys.exit(0)



def main() -> None:

    event = threading.Event()
    event.set()

    thread1 = threading.Thread(target=run_game, args=(event,))
    thread2 = threading.Thread(target=process_input, args=(event,), daemon=True)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()