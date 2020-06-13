import pygame as pg

from graphics import settings
from graphics.objects.g_object import GObject


class Inventory(GObject):
    def __init__(self, game, piece_repository, pos: pg.Rect):
        super().__init__(pos)
        self.game = game
        self.piece_repository = piece_repository
        self.PIECE_OFFSET = 4
        self.pieces = [None] * 16
        self.place_pieces()

    def calculate_piece_size(self):
        return min((self.pos.w - 3 * self.PIECE_OFFSET) // 2, (self.pos.h - 9 * self.PIECE_OFFSET) // 8)

    def place_pieces(self):
        self.update(None)
        piece_size = self.calculate_piece_size()
        rect = pg.Rect(self.pos.x + self.PIECE_OFFSET, self.pos.y + self.PIECE_OFFSET, piece_size, piece_size)
        for i in range(16):
            if i == 8:
                rect.x += piece_size + self.PIECE_OFFSET
                rect.y = self.pos.y + self.PIECE_OFFSET

            if self.pieces[i] is not None:
                self.pieces[i].move(rect.copy())
            rect.move_ip(0, self.PIECE_OFFSET + piece_size)

    def move(self, pos: pg.Rect):
        super().move(pos)
        self.place_pieces()

    def update(self, now):
        inventory = self.game.get_inventory()
        for i in range(16):
            self.pieces[i] = self.piece_repository.get_piece(inventory[i])

    def draw(self, surface: pg.Surface):
        # Only highlight selected
        selected_piece_id = self.game.get_selected_piece()
        piece = self.piece_repository.get_piece(selected_piece_id)
        if piece is None:
            return

        half_offset = self.PIECE_OFFSET // 2
        coords = pg.Rect(
            piece.pos.x - half_offset,
            piece.pos.y - half_offset,
            piece.pos.w + self.PIECE_OFFSET,
            piece.pos.h + self.PIECE_OFFSET
        )
        pg.draw.rect(surface, settings.COLORS["inventory_selected_color"], coords, half_offset)

    def clicked(self, x, y):
        if not self.game.should_select_piece():
            return

        for i in range(16):
            piece = self.pieces[i]
            if piece is not None:
                if piece.pos.collidepoint(x, y):
                    self.game.piece_selected(piece.get_id())
                    return
