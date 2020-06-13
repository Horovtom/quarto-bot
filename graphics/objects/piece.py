from graphics import settings
from graphics.objects.g_object import GObject
import pygame as pg

class Piece(GObject):
    def __init__(self, pos: pg.Rect, tall: bool, triangle:bool, hole:bool, blue: bool):
        super().__init__(pos)
        self.tall = tall
        self.triangle = triangle
        self.hole = hole
        self.blue = blue

        self.texture = self.create_texture()


    def move(self, pos: pg.Rect):
        changed = self.pos.w != pos.w or self.pos.h != pos.h
        GObject.move(self, pos)
        if changed:
            self.texture = self.create_texture()


    def create_texture(self):
        tex = pg.Surface((self.pos.w, self.pos.h))
        tex.fill(settings.COLORS["piece_background"])

        color_id = "piece_fg_{}".format("blue" if self.blue else "green")
        fg_color = settings.COLORS[color_id]
        fill = 2 if self.tall else 0
        half_x = self.pos.w // 2
        half_y = self.pos.h // 2

        if self.triangle:
            # Draw square
            dist_x = half_x - half_x // 5
            dist_y = half_y - half_y // 5
            top = [half_x, half_y - dist_y]
            left = [half_x - dist_x, half_y]
            bot = [half_x, half_y + dist_y]
            right = [half_x + dist_x, half_y]
            pg.draw.polygon(tex, fg_color, [top, right, bot, left], fill)
        else:
            # Draw circle
            pg.draw.circle(tex, fg_color, (half_x, half_y), half_x - half_x // 5, fill)

        if self.hole:
            pg.draw.circle(tex, settings.COLORS["piece_fg_hole"], (half_x, half_y), half_x // 4, 0)

        return tex

    def update(self, now):
        pass

    def draw(self, surface):
        surface.blit(self.texture, self.pos)

    def get_id(self):
        return int(self.tall) + int(self.triangle) * 2 + int(self.hole) * 4 + int(self.blue) * 8
