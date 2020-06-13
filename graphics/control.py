import pygame as pg

from graphics.game_scene import GameScene
from graphics.menu_scene import MenuScene
import graphics.settings as settings


class Control:
    """
    Contains main loop, event loop and scene switching
    """

    def __init__(self):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.state_dict = {
            "START": MenuScene("START"),
            "GAME": GameScene(),
            "END": MenuScene("END.")
        }
        self.state = self.state_dict["START"]

    def event_loop(self):
        """
        Handle quit events and pass event on to current scene.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def update(self):
        """
        Update current scene and switch if needed
        """
        now = pg.time.get_ticks()
        self.state.update(now)
        if self.state.done:
            self.state.reset()
            self.state = self.state_dict[self.state.next]

    def draw(self):
        """
        Draw the current scene if it is ready
        """

        if self.state.start_time:
            self.state.draw(self.screen)

    def display_fps(self):
        """
        Show the programs FPS in the window handle
        """

        caption = "{} - FPS: {:.2f}".format(settings.CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)

    def main_loop(self):
        """
        Run around
        """

        self.screen.fill(settings.COLORS["background"])
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)
            self.display_fps()
