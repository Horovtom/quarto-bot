import pygame as pg

from graphics import settings
from graphics.scene import Scene


class EndGameScene(Scene):
    def __init__(self):
        super().__init__("MENU")

        self.title = []
        self.who_won = []
        self.any_key = []
        self.winner = ""

    def initialize(self, *args):
        self.winner = args[0]
        self.make_text()
        self.initialized = True

    def make_text(self):
        a = settings.FONTS["big"].render("Game Finished!", True, settings.COLORS["menu_items"])
        b = a.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=settings.DRAWABLE_AREA.centery - 150)
        self.title = [a, b]
        a = settings.FONTS["big"].render("Player {} won".format(self.winner), True, settings.COLORS["menu_items"])
        b = a.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=settings.DRAWABLE_AREA.centery)
        self.who_won = [a, b]
        a = settings.FONTS["normal"].render("Press any key to continue...", True, settings.COLORS["menu_items"])
        b = a.get_rect(centerx=settings.DRAWABLE_AREA.centerx, centery=settings.DRAWABLE_AREA.centery + 200)
        self.any_key = [a, b]

    def draw(self, surface):
        surface.fill(settings.COLORS["background"])

        surface.blit(*self.title)
        surface.blit(*self.who_won)
        surface.blit(*self.any_key)

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.done = True
