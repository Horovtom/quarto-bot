import pygame as pg

from graphics import settings
from graphics.objects.g_object import GObject


class Board(GObject):
    def __init__(self, game, piece_repository, pos):
        super().__init__(pos)
        self.game = game
        self.piece_repository = piece_repository
        self.SIZE = 4
        self.CELL_MARGIN = 3
        self.cell_size = self.get_cell_size()
        self.pieces = [[None for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def update(self, now):
        board = self.game.get_board()
        cell_size = self.cell_size
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                piece = self.piece_repository.get_piece(board[x][y])
                if self.pieces[x][y] != piece:
                    self.pieces[x][y] = piece
                    rect = pg.Rect(self.pos.x + self.CELL_MARGIN + (x * (self.CELL_MARGIN + cell_size)),
                                   self.pos.y + self.CELL_MARGIN + (y * (self.CELL_MARGIN + cell_size)),
                                   cell_size, cell_size)
                    piece.move(rect)

    def get_cell_size(self):
        return (min(self.pos.w, self.pos.h) - (self.SIZE + 1) * self.CELL_MARGIN) // self.SIZE

    def move(self, pos: pg.Rect):
        super().move(pos)
        self.cell_size = self.get_cell_size()

    def get_world_coords(self, x, y):
        cell_size = self.cell_size
        x_coord = self.pos.x + self.CELL_MARGIN + (x * (self.CELL_MARGIN + cell_size))
        y_coord = self.pos.y + self.CELL_MARGIN + (y * (self.CELL_MARGIN + cell_size))
        return x_coord, y_coord

    def draw(self, surface):
        surface.fill(settings.COLORS["board"], self.pos)
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if self.pieces[x][y] is None:
                    surface.fill(settings.COLORS["empty_board_cell"],
                                 pg.Rect(*self.get_world_coords(x, y), self.cell_size, self.cell_size))

    def clicked(self, x, y):
        if not self.game.should_place_piece():
            return
        cell_size = self.cell_size
        x -= self.pos.x + self.CELL_MARGIN
        y -= self.pos.y + self.CELL_MARGIN
        x_index = x // (cell_size + self.CELL_MARGIN)
        y_index = y // (cell_size + self.CELL_MARGIN)
        if x_index >= 0 and x_index < self.SIZE and y_index >= 0 and y_index < self.SIZE and \
                self.pieces[x_index][y_index] is None:
            self.game.piece_placed(x_index, y_index)
