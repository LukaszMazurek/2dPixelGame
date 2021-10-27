import pygame

from src.settings import Settings
from src.game import Game


def main():
    pygame.init()

    pygame.display.set_caption(Settings.caption)

    screen = pygame.display.set_mode(Settings.display_size)

    Game.start(screen)


if __name__ == "__main__":
    main()


