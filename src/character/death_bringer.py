from character.chracter import Character
from character.state import State
from components.animation import Animation
from settings import Settings
from components.rectangle import Rectangle


class DeathBringer(Character):
    def __init__(self, health_points: int):
        self.__actions = dict()
        self.__position_x = 500
        self.__position_y = Settings.display_size[1] - Settings.get_ground_height() - 140
        self.__current_state = State.idle
        self.__health_points = health_points
        self.__health_bar = None
        self.__health_bar_position = None

    def set_idle(self, animation: Animation):
        self.__actions[State.idle] = animation

    def set_attacking(self, animation: Animation):
        pass

    def set_run_right(self, animation: Animation):
        pass

    def set_run_left(self, animation: Animation):
        pass

    def set_health_bar(self, rectangle: Rectangle, health_bar_position: dict):
        self.__health_bar = rectangle
        self.__health_bar_position = health_bar_position

    def __update_action(self):
        for action in self.__actions.values():
            try:
                action.set_x(self.__position_x)
                action.set_y(self.__position_y)
            except Exception as e:
                print(f"action is none build object: {e}")

    def __update_health_bar(self):
        self.__health_bar.set_x(self.__health_bar_position['x'])
        self.__health_bar.set_y(self.__health_bar_position['y'])

    def action(self):
        self.__update_action()
        self.__health_bar.blit()
        self.__actions[self.__current_state].blit()

    def get_x(self):
        return self.__position_x

    def get_y(self):
        return self.__position_y
