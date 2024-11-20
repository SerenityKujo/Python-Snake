
from bmgraphics import Sprite

class Board(Sprite):
    def __init__\
        (self, lineNumber, colNumber, y , x, screen, bkgdColor, wallColor):
        super(Board, self).__init__(lineNumber, colNumber, y, x, screen)

        self.set(0, range(colNumber), wallColor)
        self.set(range(1, lineNumber), 0, wallColor)
        self.set(range(1, lineNumber), colNumber - 1, wallColor)
        self.set(lineNumber - 1, range(colNumber), wallColor)

        self.set(range(1, lineNumber - 1), range(1, colNumber - 1), bkgdColor)

        self.display()

        self._screen = screen
        self._bkgdColor = bkgdColor
        self._wallColor = wallColor

    def bkgdColor(self):
        return self._bkgdColor

    def wallColor(self):
        return self._wallColor

