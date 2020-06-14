import graphics.settings as settings
from graphics.cursor_scene_generic import CursorSceneGeneric


class MenuScene(CursorSceneGeneric):
    """A state for the start and death scene."""

    def __init__(self):
        title = settings.CAPTION
        menu_items = [
            ("New Game", self.new_game),
            ("Rules", self.rules),
            ("Exit", self.exit)
        ]

        super().__init__(title, menu_items)
        self.reset()

    def new_game(self):
        self.next = "NEWGAME"
        self.done = True

    def rules(self):
        self.next = "RULES"
        self.done = True

    def exit(self):
        self.next = None
        self.done = True
