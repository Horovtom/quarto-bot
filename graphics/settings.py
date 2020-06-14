import pygame as pg

CAPTION = "Quarto"
SCREEN_SIZE = (720, 520)
DRAWABLE_AREA = pg.Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
BOARD_RECT = pg.Rect(10, 10, DRAWABLE_AREA.h - 20, DRAWABLE_AREA.h - 20)
INVENTORY_RECT = pg.Rect(0, 0, 0, 0)
FONTS = {}

COLORS = {
    "background": (30, 40, 50),
    "board": pg.Color("darkgreen"),
    "empty_board_cell": pg.Color("darkred"),
    "full_board_cell": pg.Color("blue"),
    "piece_background": pg.Color("black"),
    "piece_fg_blue": pg.Color("blue"),
    "piece_fg_green": pg.Color("green"),
    "piece_fg_hole": pg.Color("orange"),
    "inventory_selected_color": pg.Color("red"),
    "menu_items": pg.Color("white"),
    "menu_cursor": pg.Color("yellow")
}


def _init_inventory_rect():
    global INVENTORY_RECT

    left_border = BOARD_RECT.x + BOARD_RECT.w + 20
    right_border = SCREEN_SIZE[0] - 10
    top_border = 10
    bot_border = SCREEN_SIZE[1] - 10
    width = right_border - left_border
    height = bot_border - top_border
    INVENTORY_RECT = pg.Rect(left_border, top_border, width, height)


def initialize():
    global FONTS, INVENTORY_RECT
    FONTS = {
        "normal": pg.font.SysFont("helvetica", 30, False),
        "big": pg.font.SysFont("helvetica", 50, True),
        "small": pg.font.SysFont("Times New Roman", 17, False)
    }
    _init_inventory_rect()
