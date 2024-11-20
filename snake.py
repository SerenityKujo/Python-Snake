
from board import Board
from direction import Direction
from collections import deque, namedtuple
from time import monotonic

class Snake:
    def __init__(self, board, y , x, aliveColor, deadColor, foodColor):
        super(Board, board).set(y, x, aliveColor)

        self._board = board
        self._aliveColor = aliveColor
        self._deadColor = deadColor
        self._foodColor = foodColor
        self._direction = Direction.RIGHT
        self._parts = deque([[y, x]])
        self._speed = 10
        self._alive = True

    def aliveColor(self):
        return self._aliveColor

    def foodColor(self):
        return self._foodColor

    def speed(self):
        return self._speed

    def alive(self):
        return self._alive

    def size(self):
        return len(self._parts)

    _Cell = namedtuple('Cell', 'y x color')
    def _nextCell(self):
        headCoords = self._parts[len(self._parts) - 1]

        if self._direction == Direction.UP:
            y = headCoords[0] - 1
            x = headCoords[1]
        elif self._direction == Direction.DOWN:
            y = headCoords[0] + 1
            x = headCoords[1]
        elif self._direction == Direction.LEFT:
            y = headCoords[0]
            x = headCoords[1] - 1
        else:
            y = headCoords[0]
            x = headCoords[1] + 1

        return Snake._Cell(y, x, self._board._bitmap[y][x])

    def _die(self):
        then = monotonic()
        partIndex = len(self._parts) - 1

        while partIndex >= 0:
            if monotonic() - then >= 0.05:
                self._board.set\
                (\
                    self._parts[partIndex][0], self._parts[partIndex][1],
                    self._deadColor\
                )
                self._board.display\
                (self._parts[partIndex][0], self._parts[partIndex][1])
                partIndex -= 1
                then = monotonic()
        self._alive = False

    def changeDir(self, direction):
        def opposite(direction):
            if direction == Direction.UP:
                return Direction.DOWN
            elif direction == Direction.DOWN:
                return Direction.UP
            elif direction == Direction.LEFT:
                return Direction.RIGHT
            else:
                return Direction.LEFT

        if self._direction != opposite(direction):
            self._direction = direction

    def move(self):
        nextCell = self._nextCell()

        if nextCell.color == self._foodColor:
            self._parts.append([nextCell.y, nextCell.x])
            self._board.set(nextCell.y, nextCell.x, self._aliveColor)
            self._board.display(nextCell.y, nextCell.x)
            if len(self._parts) % 5 == 0:
                    self._speed += 0.2
        elif nextCell.color == self._board.bkgdColor():
            self._parts.append([nextCell.y, nextCell.x])
            self._board.set(nextCell.y, nextCell.x, self._aliveColor)
            self._board.display(nextCell.y, nextCell.x)
            popPartCoords = self._parts.popleft()
            self._board.set\
            (\
                popPartCoords[0], popPartCoords[1],\
                self._board._bkgdColor\
            )
            self._board.display(popPartCoords[0], popPartCoords[1])
        elif nextCell.color == self._board.wallColor() or\
             nextCell.color == self._aliveColor:
            self._die()

