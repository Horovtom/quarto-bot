from typing import Optional, List

from logic.board import Board
from logic.stack import Stack


class Game:
    def __init__(self, human_players):
        self.board = Board()
        self.stack = Stack()

        self.human_players = human_players
        print("Initialized with human players: {}".format(self.human_players))
        self.player_on_turn = 0
        self.selected_piece = None
        self.player_won = None

    def is_interactive_step(self):
        return True

    def should_place_piece(self) -> bool:
        return self.selected_piece is not None

    def should_select_piece(self) -> bool:
        return self.selected_piece is None

    def piece_selected(self, piece_id):
        if not self.stack.contains_piece(piece_id):
            return

        self.selected_piece = piece_id
        self.stack.remove_piece(self.selected_piece)

    def piece_placed(self, x, y):
        if not self.board.is_free_place(x, y):
            return
        self.board.place(x, y, self.selected_piece)
        self.selected_piece = None

        if self.check_win(x, y):
            self.notify_won()
        else:
            self.swap_player()

    def notify_won(self):
        self.player_won = self.player_on_turn
        print("Player {} won!".format(self.player_won))

    def swap_player(self):
        self.player_on_turn = (self.player_on_turn + 1) % 2

    def check_win(self, x, y):
        for j in range(4):
            prop = 2 ** j

            count_row = count_col = count_rtlb = count_ltrb = 0
            tiles_row = tiles_col = tiles_rtlb = tiles_ltrb = 0
            for i in range(4):
                if not self.board.is_free_place(i, y):
                    tiles_row += 1
                if not self.board.is_free_place(x, i):
                    tiles_col += 1
                if not self.board.is_free_place(i, 3 - i):
                    tiles_rtlb += 1
                if not self.board.is_free_place(i, i):
                    tiles_ltrb += 1

                if self.board.has_property(i, y, prop):
                    count_row += 1
                if self.board.has_property(x, i, prop):
                    count_col += 1
                if self.board.has_property(i, 3 - i, prop):
                    count_rtlb += 1
                if self.board.has_property(i, i, prop):
                    count_ltrb += 1

            if (count_row % 4 == 0 and tiles_row == 4) or (count_col % 4 == 0 and tiles_col == 4) or (
                    count_rtlb % 4 == 0 and tiles_rtlb == 4) or (count_ltrb % 4 == 0 and tiles_ltrb == 4):
                return True
        return False

    def get_board(self) -> List[List[Optional[int]]]:
        return self.board.get()

    def get_inventory(self) -> List[Optional[int]]:
        return self.stack.get()

    def get_selected_piece(self):
        return self.selected_piece

    def someone_won(self):
        return self.player_won is not None
