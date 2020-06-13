import copy
from typing import Optional, List


class Board:
    def __init__(self):
        self.board = self.clear()

    def clear(self):
        self.board = [[None for _ in range(4)] for _ in range(4)]
        return self.board

    def get(self) -> List[List[Optional[int]]]:
        return copy.deepcopy(self.board)

    def place(self, x, y, selected_piece):
        self.board[x][y] = selected_piece

    def is_free_place(self, x, y):
        return self.board[x][y] is None

    def has_property(self, x, y, prop):
        return self.board[x][y] is not None and self.board[x][y] & prop > 0
