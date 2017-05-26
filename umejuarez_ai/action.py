import time
import random

from threading import Thread
from .options import STANCES, SPECIALS, NORMALS
from pykeyboard import PyKeyboard
from .state import State

initial = {
    "own": {
        "stance": STANCES["standing"],
        "action": None
    }
}

kb = PyKeyboard()
class Mover(object):
    def __init__(self):
        State(initial)

    def choose_stance(self):
        state = State({})

        if random.random() < 0.7:
            stance = state.get_stance()
        else:
            stance = random.sample(list(STANCES.values()), 1)[0]

        return stance

    def choose_action(self):
        roll = random.random()
        if roll < 0.7:
            action = None
        elif roll < 0.85:
            action = random.sample(SPECIALS, 1)[0]
        else:
            action = random.sample(NORMALS, 1)[0]

        return action

    def move(self):
        state = State({})
        if state.acting():
            return

        current_stance = state.get_stance()
        next_stance = self.choose_stance()

        action = self.choose_action()
        if action is None:
            release_combination(current_stance)
            press_combination(next_stance)
            State({"own": {"stance": next_stance}})
        else:
            self.send_action(action, current_stance, next_stance)

    def send_action(self, action, current_stance, next_stance):
        def act():
            print("Acting!")
            State({"own": {"acting": True}})
            release_combination(current_stance)
            tap_sequence(action)
            press_combination(next_stance)
            State({"own": {"stance": next_stance, "acting": False}})
            print("Finished acting!")

        t = Thread(target=act)
        t.start()

def press_combination(combination):
    for key in combination:
        kb.press_key(key)

def release_combination(combination):
    for key in combination:
        kb.release_key(key)

def tap_sequence(sequence):
    for combination in sequence:
        print(combination)
        press_combination(combination)
        time.sleep(.1)
        release_combination(combination)
