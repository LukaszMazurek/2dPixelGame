from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build_right_move_animation(self):
        pass

    @abstractmethod
    def build_left_move_animation(self):
        pass

    @abstractmethod
    def build_attacking_animation(self):
        pass

    @abstractmethod
    def build_idle_animation(self):
        pass

    @abstractmethod
    def get_character(self):
        pass
