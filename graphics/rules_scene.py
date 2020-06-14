import pygame as pg

from graphics import settings
from graphics.scene import Scene


class RulesScene(Scene):

    def __init__(self):
        super().__init__("MENU")

        self.title = []
        self.text = []
        self.any_key = []
        self.rules_text = ""
        with open("rules.txt", 'r') as f:
            self.rules_text = f.readlines()

    def initialize(self, *args):
        self.make_text()
        self.initialized = True

    def make_text(self):
        a = settings.FONTS["normal"].render("Rules", True, settings.COLORS["menu_items"])
        b = a.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=20 + a.get_rect().h // 2)
        self.title = [a, b]
        self.text = []
        offset = b.y + b.h + 10
        for line in self.rules_text:
            a = settings.FONTS["small"].render(line.strip(), True, settings.COLORS["menu_items"])
            b = a.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=offset)
            offset += b.h + 2
            self.text.append([a, b])

        a = settings.FONTS["normal"].render("Press any key to continue...", True, settings.COLORS["menu_items"])
        b = a.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=offset + 10)
        self.any_key = [a, b]

    def draw(self, surface):
        surface.fill(settings.COLORS["background"])
        surface.blit(*self.title)
        for line in self.text:
            surface.blit(*line)
        surface.blit(*self.any_key)

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.done = True
