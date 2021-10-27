import pygame

from abc import abstractmethod


class Component(pygame.sprite.Sprite):
    @abstractmethod
    def blit(self):
        pass

    @abstractmethod
    def set_x(self, x: int):
        pass

    @abstractmethod
    def set_y(self, y: int):
        pass
