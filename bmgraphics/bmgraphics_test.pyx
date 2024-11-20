
from bmgraphics.general import init_bmgraphics, setBackground, end_bmgraphics
from curses import curs_set
from sys import argv
from bmgraphics.sprite import Sprite
from bmgraphics.color import Color

def test(argv):
    stdscr = init_bmgraphics()
    curs_set(False)

    setBackground(stdscr, Color.L_GREY)

    if len(argv) == 2:
        image = Sprite(argv[1], 1, 1, stdscr)
    else:
        from curses import COLS, LINES
        image = Sprite(1, 1, LINES // 2, COLS // 4, stdscr)
        image.set(range(1), range(1), Color.BLACK)

    image.display()

    stdscr.getch()

    end_bmgraphics()

    exit(0)

