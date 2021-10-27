import pygame

from components.component import Component


class Rectangle(Component):
    def __init__(self, screen, x: int, y: int, width: int, height: int, color: tuple):
        super(Rectangle, self).__init__()
        self.screen = screen
        self.screen = screen
        self.__width = width
        self.__height = height
        self.__rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.__rect.y = y
        self.__rect.x = x
        self.__color = color

    def blit(self) -> None:
        pygame.draw.rect(self.screen, self.__color, self.__rect)

    def set_x(self, x: int):
        self.__rect.x = x

    def set_y(self, y: int):
        self.__rect.y = y
