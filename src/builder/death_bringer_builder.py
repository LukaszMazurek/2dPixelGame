from builder.builder import Builder
from character.death_bringer import DeathBringer
from components.animation import Animation
from components.colors import Colors
from components.rectangle import Rectangle


class DeathBringerBuilder(Builder):

    def __init__(self, screen):
        self.health_points = 100
        self.screen = screen
        self.death_bringer = DeathBringer(self.health_points)

    def build_left_move_animation(self):
        # TODO implement left move
        pass

    def build_attacking_animation(self):
        # TODO implement attack
        pass

    def build_idle_animation(self):
        animation = Animation(self.screen, "src/assets/death_bringer/idle_150", "Bringer-of-Death_Idle", 8)
        self.death_bringer.set_idle(animation)

    def build_right_move_animation(self):
        # TODO implement right move
        pass

    def prepare_health_bar(self):
        x = self.death_bringer.get_x() + 110
        y = self.death_bringer.get_y() + 40
        rectangle = Rectangle(self.screen, x, y, self.health_points, 10, Colors.red)
        self.death_bringer.set_health_bar(rectangle, {'x': x, 'y': y})

    def get_character(self):
        return self.death_bringer


