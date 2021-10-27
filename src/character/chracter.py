from abc import ABC, abstractmethod
from components.animation import Animation


class Character(ABC):
    @abstractmethod
    def set_idle(self, animation: Animation):
        pass

    @abstractmethod
    def set_attacking(self, animation: Animation):
        pass

    @abstractmethod
    def set_run_right(self, animation: Animation):
        pass

    @abstractmethod
    def set_run_left(self, animation: Animation):
        pass
