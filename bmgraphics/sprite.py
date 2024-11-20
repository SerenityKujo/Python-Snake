
from bmgraphics.general import dispColSquare
from bmgraphics.color import Color

class Sprite(object):
    def _toColor(self, colorChar):
        if colorChar == 't': return Color.NONE
        elif colorChar == 'r': return Color.RED
        elif colorChar == 's': return Color.L_RED
        elif colorChar == 'g': return Color.GREEN
        elif colorChar == 'h': return Color.L_GREEN
        elif colorChar == 'o': return Color.ORANGE
        elif colorChar == 'p': return Color.L_ORANGE
        elif colorChar == 'u': return Color.BLUE
        elif colorChar == 'v': return Color.L_BLUE
        elif colorChar == 'm': return Color.MAGENTA
        elif colorChar == 'n': return Color.L_MAGENTA
        elif colorChar == 'y': return Color.CYAN
        elif colorChar == 'z': return Color.L_CYAN
        elif colorChar == 'e': return Color.GREY
        elif colorChar == 'f': return Color.L_GREY
        elif colorChar == 'a': return Color.BLACK
        elif colorChar == 'b': return Color.L_BLACK

    def __init__(self, *args):
        # TODO Cases when file badly formatted
        argsLen = len(args)
        if argsLen == 4:
            bitMapFile = open(args[0], 'r')

            self._height, self._width  = \
            (int(s) for s in bitMapFile.readline().split())
            self._bitmap =\
            [\
                [ [] for c in range(self._width)]\
                for l in range(self._height)\
            ]

            for l in range(self._height):
                line = bitMapFile.readline()
                for c in range(self._width):
                    self._bitmap[l][c] = self._toColor(line[c])

            bitMapFile.close()

        elif argsLen == 5:
            self._height, self._width = args[0], args[1]
            self._bitmap =\
            [\
                [ [] for c in range(self._width)]\
                for l in range(self._height)\
            ]

        self._y = args[-3]
        self._x = args[-2]
        self._screen = args[-1]

    def set(self, lineArg, colArg, color):
        def toIterable(argument):
            if type(argument) == range:
                return argument
            else:
                return [argument]

        for l in toIterable(lineArg):
            for c in toIterable(colArg):
                self._bitmap[l][c] = color

    def display(self, *args):
        argsLen = len(args)
        if argsLen == 0:
            for l in range(self._height):
                for c in range(self._width):
                    dispColSquare\
                    (\
                        self._y + l, self._x + c, self._screen, self._bitmap[l][c]
                    )
            self._screen.refresh()

        elif argsLen == 2:
            l = args[0]
            c = args[1]
            dispColSquare\
            (\
                self._y + l, self._x + c, self._screen, self._bitmap[l][c]
            )
            self._screen.refresh()


