import pygame

from src.settings import Settings
from src.game import Game


def main():

    """initialize logger"""
    Settings.logger = Settings.set_logger()
    Settings.logger.debug("start")

    pygame.init()

    pygame.display.set_caption(Settings.caption)

    screen = pygame.display.set_mode(Settings.display_size)

    Game.start(screen)


if __name__ == "__main__":
    main()


