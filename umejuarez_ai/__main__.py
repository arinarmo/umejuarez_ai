import cv2

from .input import Stream
from .action import Mover

from .state import State

def callback(mover):
    state = State({})
    mover.move()
    cv2.imshow("frame", state.instance._value["frame"].frame)
    cv2.waitKey(16)
    ("Frame number: #{n}, Healths: {own}, {enemy}".format(
        n = state.instance._value["frame_number"],
        own = int(state.instance._value["own"]["health"]*100),
        enemy = int(state.instance._value["enemy"]["health"]*100)
    ))

    return state


if __name__ == "__main__":
    filename = "/home/adolfo/output.flv"
    stream = Stream()
    stream.run(filename, callback, mover=Mover())