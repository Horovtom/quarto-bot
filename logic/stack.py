import copy
from typing import Optional, List


class Stack:
    def __init__(self):
        self.stack = self.reset()

    def reset(self):
        self.stack = list(range(16))
        return self.stack

    def get(self) -> List[Optional[int]]:
        return copy.deepcopy(self.stack)

    def contains_piece(self, piece_id):
        if piece_id is None:
            return True
        return piece_id in self.stack

    def remove_piece(self, selected_piece):
        for i in range(16):
            if self.stack[i] == selected_piece:
                self.stack[i] = None
                return

