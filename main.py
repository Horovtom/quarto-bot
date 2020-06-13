import sys

import pygame as pg
import graphics


def main():
    """
    Prepare pygame, our screen and start the program
    """

    pg.init()
    pg.display.set_caption(graphics.settings.CAPTION)
    pg.display.set_mode(graphics.settings.SCREEN_SIZE)
    graphics.settings.initialize()

    graphics.Control().main_loop()

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
