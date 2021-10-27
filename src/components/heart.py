import pygame

from components.component import Component


class Heart(Component):
    def __init__(self, screen, path: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.__path = path
        self.__heart_image = self.load_image()
        self.__x = x
        self.__y = y

    def load_image(self):
        return pygame.image.load(f"{self.__path}.png")

    def blit(self):
        position = (self.__x, self.__y)
        self.__screen.blit(self.__heart_image, position)

    def set_x(self, x: int):
        self.__x = x

    def set_y(self, y: int):
        pass
