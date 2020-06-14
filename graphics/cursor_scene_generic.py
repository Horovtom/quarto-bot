from typing import List, Callable, Tuple

import pygame as pg
import abc
from graphics import settings
from graphics.scene import Scene


class CursorSceneGeneric(Scene, abc.ABC):
    def __init__(self, title, menu_items: List[Tuple[str, Callable]]):
        super().__init__()

        self.cursor = 0
        self.title_text = title
        self.menu_items = menu_items
        self.menu_items_draw = []
        self.title = []

    def reset(self):
        super().reset()
        self.cursor = 0
        self.menu_items_draw = []

    def make_text(self):
        title = settings.FONTS["big"].render(self.title_text, True, settings.COLORS["menu_items"])
        rect = title.get_rect(centerx=settings.DRAWABLE_AREA.centerx,
                              centery=settings.DRAWABLE_AREA.y + settings.DRAWABLE_AREA.h // 8)
        self.title = [title, rect]

        offset = 0
        starty = rect.y + rect.h + 30
        for item in self.menu_items:
            text_sprite = settings.FONTS["normal"].render(item[0], True, settings.COLORS["menu_items"])
            rect = text_sprite.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=starty + offset)
            offset += text_sprite.get_rect().h + 10
            self.menu_items_draw.append([text_sprite, rect])

    def draw(self, surface):
        surface.fill(settings.COLORS["background"])
        surface.blit(*self.title)
        for item in self.menu_items_draw:
            surface.blit(*item)

        # Draw cursor
        text_rect = self.menu_items_draw[self.cursor][1]
        pg.draw.circle(surface, settings.COLORS["menu_cursor"], (text_rect.x - text_rect.h, text_rect.centery),
                       text_rect.h // 5, 0)

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                self.cursor = min(self.cursor + 1, len(self.menu_items) - 1)
            elif event.key == pg.K_UP:
                self.cursor = max(self.cursor - 1, 0)
            elif event.key == pg.K_RETURN:
                self.menu_items[self.cursor][1]()

    def initialize(self, *args):
        if len(args) == 2:
            self.title = args[0]
            self.menu_items = args[1]
        self.make_text()
        self.initialized = True
