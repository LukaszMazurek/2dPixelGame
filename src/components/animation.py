import pygame

from pathlib import Path
from components.component import Component


class Animation(Component):
    def __init__(self, screen, asset_path: str, asset_name: str, frames: int, start_x=0, start_y=0):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.__path = asset_path
        self.__name = asset_name
        self.__frames = frames
        self.__x = start_x
        self.__y = start_y
        self.__images = self.load_images()
        self.__current = 0

    def load_images(self) -> list:

        images = list()

        for idx in range(1, self.__frames + 1):
            path = Path(f"{self.__path}/{self.__name}_{idx}.png")
            images.append(pygame.image.load(path))

        return images

    def blit(self) -> None:
        self.__current += 1

        if self.__current == len(self.__images):
            self.__current = 0

        position = (self.__x, self.__y)

        self.__screen.blit(self.__images[self.__current], position)

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y



