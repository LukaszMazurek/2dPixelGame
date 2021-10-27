from components.animation import Animation
from components.heart import Heart
from src.settings import Settings
from character.chracter import Character
from character.state import State


class Warrior(Character):
    def __init__(self):
        self.__actions = dict()
        self.__position_x = 0
        self.__position_y = Settings.display_size[1] - Settings.get_ground_height() - 66
        self.__health_points = 1
        self.__hearts = []
        self.__current_state = State.idle
        self.__movement_speed = 8

    def change_state(self, state: State):
        self.__current_state = state

    def __show_healths(self):
        for heart in self.__hearts:
            heart.blit()

    def __update(self):
        for action in self.__actions.values():
            try:
                action.set_x(self.__position_x)
                action.set_y(self.__position_y)
            except Exception as e:
                print(f"action is none build object: {e}")

    def action(self):
        self.__update()

        if self.__current_state == State.running_right:
            self.__position_x += self.__movement_speed
        if self.__current_state == State.running_left:
            self.__position_x -= self.__movement_speed

        self.__show_healths()
        self.__actions[self.__current_state].blit()

    def get_current_state(self):
        return self.__current_state

    def set_idle(self, animation: Animation) -> None:
        self.__actions[State.idle] = animation

    def set_attacking(self, animation: Animation) -> None:
        self.__actions[State.attacking] = animation

    def set_run_right(self, animation: Animation) -> None:
        self.__actions[State.running_right] = animation

    def set_run_left(self, animation: Animation) -> None:
        self.__actions[State.running_left] = animation

    def add_heart(self, heart: Heart):
        self.__hearts.append(heart)

    def remove_heart(self):
        self.__hearts.pop()
