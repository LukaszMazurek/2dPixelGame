from enum import Enum


class State(Enum):
    idle = 0
    running_right = 1
    running_left = 2
    attacking = 4
    stop = -1
