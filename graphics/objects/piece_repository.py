import pygame as pg

from graphics.objects.g_object import GObject
from graphics.objects.piece import Piece


class PieceRepository(GObject):
    def __init__(self, pos: pg.Rect):
        super().__init__(pos)
        self.piece_size = 200
        self.pieces = self.create_pieces()

    def create_pieces(self):
        pieces = []

        rect = pg.Rect(0, 0, self.piece_size, self.piece_size)
        for i in range(16):
            pieces.append(Piece(rect.copy(), bool(i & 1),bool(i & 2), bool(i & 4) , bool(i & 8)))

        return pieces

    def get_piece(self, id):
        if id is None or id < 0 or id >= 16:
            return None
        return self.pieces[id]

    def update(self, now):
        for piece in self.pieces:
            piece.update(now)

    def draw(self, surface: pg.Surface):
        for piece in self.pieces:
            piece.draw(surface)
