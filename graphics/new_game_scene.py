from graphics.cursor_scene_generic import CursorSceneGeneric


class NewGameScene(CursorSceneGeneric):
    def __init__(self):
        title = "New Game"
        menu_items = [
            ("Hot Seat", self.hot_seat),
            ("With Bot", self.one_bot),
            ("Two Bots", self.two_bots),
            ("Back", self.back)
        ]

        super().__init__(title, menu_items)

        self.reset()

    def hot_seat(self):
        self.switch_to_game(2)

    def one_bot(self):
        self.switch_to_game(1)

    def two_bots(self):
        self.switch_to_game(0)

    def switch_to_game(self, human_players):
        self.next = "GAME"
        self.next_args = human_players
        self.done = True

    def back(self):
        self.next = "MENU"
        self.done = True
