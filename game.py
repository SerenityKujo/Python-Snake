
from bmgraphics import init_bmgraphics, setBackground, end_bmgraphics, Color
from curses import noecho, curs_set, init_pair, color_pair, A_BOLD, A_REVERSE,\
                   KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from board import Board
from snake import Snake
from random import randint
from direction import Direction
from time import monotonic

class Game:
    def __init__(self):
        self._stdscr = init_bmgraphics()
        noecho()
        curs_set(False)
        self._stdscr.nodelay(True)
        self._stdscr.keypad(True)

        setBackground(self._stdscr, Color.L_GREY)

        from curses import LINES, COLS
        lineNumber, colNumber = LINES - 6, (COLS - 12) // 2

        self._board =\
        Board\
        (\
            lineNumber, colNumber, 3, 3, self._stdscr, Color.L_GREY,\
            Color.L_ORANGE
        )

        self._snake =\
        Snake\
        (\
            self._board, lineNumber // 2, colNumber // 2, Color.L_GREEN, Color.RED,
            Color.L_CYAN\
        )
        self._score = 0

    def _setFood(self):
        self._foodY = randint(1, self._board._height - 2)
        self._foodX = randint(1, self._board._width - 2)

        # TODO Change method when there are few squares left ?
        while\
        self._board._bitmap[self._foodY][self._foodX] ==\
        self._snake.aliveColor():
            self._foodY = randint(1, self.__board.height - 2)
            self._foodX = randint(1, self.__board.width - 2)

        self._board.set(self._foodY, self._foodX, self._snake.foodColor())
        self._board.display(self._foodY, self._foodX)

    def _dispScore(self):
        init_pair(9, 7, 0)
        # FIXME CHECK
        self._stdscr.addstr\
        (\
            2, self._board._width * 2, str(self._score).rjust(6, ' '),\
            color_pair(9) | A_BOLD | A_REVERSE\
        )

    def _foodEaten(self):
        return\
            self._board._bitmap[self._foodY][self._foodX] !=\
            self._snake.foodColor()

    def _maxSteps(self):
        return len(self._board._bitmap) + len(self._board._bitmap[0]) - 6

    def _removeFood(self):
        self._board.set(self._foodY, self._foodX, self._board.bkgdColor())
        self._board.display(self._foodY, self._foodX)

    def play(self):
        self._setFood()
        self._dispScore()
        then = monotonic()

        steps = 0
        eatSteps = 0

        EAT_STEPS_WAIT = 2
        nextDirection = Direction.RIGHT

        while self._snake.alive():
            # TODO CHANGE METHOD OF PROCESSING INPUT ?
            key = self._stdscr.getch()
            if key == KEY_UP:
                nextDirection = Direction.UP
            elif key == KEY_DOWN:
                nextDirection = Direction.DOWN
            elif key == KEY_LEFT:
                nextDirection = Direction.LEFT
            elif key == KEY_RIGHT:
                nextDirection = Direction.RIGHT

            if monotonic() - then >= 1 / self._snake.speed():
                steps += 1
                self._snake.changeDir(nextDirection)
                self._snake.move()

                if self._foodEaten():
                    if eatSteps == 0:
                        self._score += self._snake.speed() * 10
                        self._dispScore()
                    eatSteps += 1
                    if eatSteps == EAT_STEPS_WAIT:
                        self._setFood()
                        eatSteps = 0
                        steps = 0

                elif steps == self._maxSteps():
                    steps = 0
                    self._removeFood()
                    self._setFood()

                then = monotonic()

        self._stdscr.nodelay(False)
        self._stdscr.getch()

        end_bmgraphics()

if __name__ == '__main__':
    game = Game()
    game.play()
    exit(0)

