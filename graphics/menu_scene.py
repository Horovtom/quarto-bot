import pygame as pg

import graphics.settings as settings
from graphics.scene import Scene


class MenuScene(Scene):
    """A state for the start and death scene."""

    def __init__(self, title):
        Scene.__init__(self, "GAME")
        self.blink_timer = 0.0
        self.blink = False
        self.make_text(title)
        self.reset()

    def make_text(self, title):
        """Pre-render text."""
        self.main = settings.FONTS["normal"].render(title, True, pg.Color("white"))
        self.main_rect = self.main.get_rect(centerx=settings.DRAWABLE_AREA.centerx,
                                            centery=settings.DRAWABLE_AREA.centery - 150)
        text = "Press any key"
        self.ne_key = settings.FONTS["normal"].render(text, True, pg.Color("white"))
        self.ne_key_rect = self.ne_key.get_rect(centerx=settings.DRAWABLE_AREA.centerx,
                                                centery=settings.DRAWABLE_AREA.centery + 150)

    def draw(self, surface):
        """Draw primary text and blinking prompt if necessary."""
        surface.fill(settings.COLORS["background"])
        surface.blit(self.main, self.main_rect)
        if self.blink:
            surface.blit(self.ne_key, self.ne_key_rect)

    def update(self, now):
        """Update blinking prompt."""
        Scene.update(self, now)
        if now - self.blink_timer > 1000.0 / 2:
            self.blink = not self.blink
            self.blink_timer = now

    def get_event(self, event):
        """Switch to game on keydown."""
        if event.type == pg.KEYDOWN:
            self.done = True
