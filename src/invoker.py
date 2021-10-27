from builder.builder import Builder


class Invoker(object):
    def __init__(self):
        self.__builder = None

    @property
    def builder(self) -> Builder:
        return self.builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self.__builder = builder

    def build_warrior(self):
        self.__builder.build_left_move_animation()
        self.__builder.build_attacking_animation()
        self.__builder.build_idle_animation()
        self.__builder.build_right_move_animation()
        self.__builder.add_hearts()

    def build_death_bringer(self):
        self.__builder.build_idle_animation()
        self.__builder.prepare_health_bar()
