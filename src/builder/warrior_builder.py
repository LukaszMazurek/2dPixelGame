from builder.builder import Builder
from character.warrior import Warrior
from components.animation import Animation
from components.heart import Heart


class WarriorBuilder(Builder):

    def __init__(self, screen):
        self.screen = screen
        self.warrior = Warrior()

    def build_left_move_animation(self):
        animation = Animation(self.screen, "src\\assets\\warrior\\run_150_left", "Warrior_Run", 8)
        self.warrior.set_run_left(animation)

    def build_attacking_animation(self):
        animation = Animation(self.screen, "src\\assets\\warrior\\attack_150", "Warrior_Attack", 12)
        self.warrior.set_attacking(animation)

    def build_idle_animation(self):
        animation = Animation(self.screen, "src\\assets\\warrior\\idle_150", "Warrior_Idle", 6)
        self.warrior.set_idle(animation)

    def build_right_move_animation(self):
        animation = Animation(self.screen, "src\\assets\\warrior\\run_150_right", "Warrior_Run", 8)
        self.warrior.set_run_right(animation)

    def add_hearts(self):
        self.warrior.add_heart(Heart(self.screen, "src\\assets\\heart\\heart", -40, -30))
        self.warrior.add_heart(Heart(self.screen, "src\\assets\\heart\\heart", 10, -30))
        self.warrior.add_heart(Heart(self.screen, "src\\assets\\heart\\heart", 60, -30))

    def get_character(self) -> Warrior:
        return self.warrior
