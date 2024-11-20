
# TODO CHECK ARGUMENTS
from curses import initscr, start_color, init_pair, endwin, color_pair, A_BOLD,\
                   A_NORMAL, A_REVERSE
from bmgraphics.color import Color

"""
Initiate the graphical library

returns ?
"""
def init_bmgraphics():
    stdscr = initscr()
    start_color()

    from curses import COLORS
    for color in range(1, COLORS):
        init_pair(color, color, 0)

    return stdscr

"""
 the graphical library

returns ?
"""
def end_bmgraphics():
    endwin()

"""
Convert???
"""

def _toAttributes(color):
    if color is None:
        pass #Exception
    return\
        (A_BOLD if color.value > 8 else A_NORMAL) |\
        (color_pair(color.value - 8 if color.value > 8 else color.value)) |\
        A_REVERSE

"""
Set colour of background
"""

def setBackground(screen, color):
    screen.attron(_toAttributes(color))
    lines, cols = screen.getmaxyx()
    for l in range(lines):
        screen.move(l, 0)
        screen.hline(ord(' '), cols)

"""
Display a square with a specific colour at coordinates (line, column)
"""
def dispColSquare(line, column, screen, color):
    if color is not Color.NONE:
        screen.addstr(line, 2 * column, "  ", _toAttributes(color))

