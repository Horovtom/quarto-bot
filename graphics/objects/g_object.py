import abc
import pygame as pg

class GObject(abc.ABC):
    def __init__(self, pos: pg.Rect):
        self.pos: pg.Rect = pos

    @abc.abstractmethod
    def update(self, now):
        pass

    @abc.abstractmethod
    def draw(self, surface: pg.Surface):
        pass

    def move(self, pos: pg.Rect):
        self.pos = pos