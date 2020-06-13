from typing import Optional

import pygame as pg

import graphics.settings as settings
from graphics.objects.board import Board
from graphics.objects.inventory import Inventory
from graphics.objects.piece_repository import PieceRepository
from graphics.scene import Scene
from logic.game import Game


class GameScene(Scene):
    """
    This scene is active during the gameplay phase
    """

    def __init__(self):
        Scene.__init__(self, "END")

        self.game = None
        self.board: Optional[Board] = None
        self.inventory: Optional[Inventory] = None
        self.piece_repository : Optional[PieceRepository] = None
        self.reset()

    def reset(self):
        """
        Prepare for next run
        """
        Scene.reset(self)
        self.game = Game()
        self.piece_repository = PieceRepository(settings.BOARD_RECT)
        self.board = Board(self.game, self.piece_repository, settings.BOARD_RECT)
        self.inventory = Inventory(self.game, self.piece_repository, settings.INVENTORY_RECT)

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONUP and self.game.is_interactive_step():
            pos = pg.mouse.get_pos()
            if self.game.should_select_piece():
                # We need to select a piece
                if self.inventory.pos.collidepoint(*pos):
                    self.inventory.clicked(*pos)

            if self.game.should_place_piece():
                # We need to place it onto the board
                if self.board.pos.collidepoint(*pos):
                    self.board.clicked(*pos)

    def update(self, now):
        Scene.update(self, now)
        if self.game.someone_won():
            self.done = True

        self.board.update(now)
        self.inventory.update(now)
        self.piece_repository.update(now)

    def draw(self, surface):
        surface.fill(settings.COLORS["background"])

        self.board.draw(surface)
        self.inventory.draw(surface)
        self.piece_repository.draw(surface)
