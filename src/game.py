import pygame

from src.settings import Settings
from src.invoker import Invoker

from components.colors import Colors
from components.rectangle import Rectangle
from character.warrior import Warrior
from character.death_bringer import DeathBringer
from  character.state import State
from builder.warrior_builder import WarriorBuilder
from builder.death_bringer_builder import DeathBringerBuilder


class Game(object):

    is_active = True

    key_down_actions = {
        pygame.K_RIGHT: State.running_right,
        pygame.K_LEFT: State.running_left,
        pygame.K_SPACE: State.attacking
    }

    key_up_actions = {
        pygame.K_RIGHT: State.idle,
        pygame.K_LEFT: State.idle,
        pygame.K_SPACE: State.idle,
        pygame.K_ESCAPE: State.idle
    }

    @staticmethod
    def get_warrior(screen, invoker: Invoker) -> Warrior:
        warrior_builder = WarriorBuilder(screen)
        invoker.builder = warrior_builder
        invoker.build_warrior()
        return warrior_builder.get_character()

    @staticmethod
    def get_death_bringer(screen, invoker: Invoker) -> DeathBringer:
        death_bringer_builder = DeathBringerBuilder(screen)
        invoker.builder = death_bringer_builder
        invoker.build_death_bringer()
        return death_bringer_builder.get_character()

    @staticmethod
    def key_down(event, warrior: Warrior) -> None:
        if Game.key_up_actions.get(event.key) is not None:
            warrior.change_state(Game.key_down_actions[event.key])

    @staticmethod
    def key_up(event, warrior: Warrior) -> None:
        if Game.key_up_actions.get(event.key) is not None:
            warrior.change_state(Game.key_up_actions[event.key])

    @staticmethod
    def event_handler(warrior: Warrior):
        """
        :return int: 0 if user want to quit PixelGame2d and 1 to play
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Game.is_active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game.is_active = False
                else:
                    Game.key_down(event, warrior)
            elif event.type == pygame.KEYUP:
                Game.key_up(event, warrior)

    @staticmethod
    def start(screen):

        clock = pygame.time.Clock()
        ground = Rectangle(screen, 0,
                           Settings.display_size[1] - Settings.get_ground_height(),
                           Settings.get_ground_width(),
                           Settings.get_ground_height(),
                           Colors.green)

        invoker = Invoker()
        ula = Game.get_warrior(screen, invoker)
        death_bringer = Game.get_death_bringer(screen, invoker)

        while Game.is_active:
            Game.event_handler(ula)

            screen.fill(Colors.blue)
            ground.blit()

            ula.action()
            death_bringer.action()

            clock.tick(Settings.frame_rate)
            pygame.display.flip()
