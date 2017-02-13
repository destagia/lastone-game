import lastone
from lastone.point import Point

_positions = [(x, y) for y in range(lastone.BOARD_SIZE) for x in range(y)]
_moves = [(Point(x1, y1), Point(x2, y2)) for x1, y1 in _positions for x2, y2 in _positions]

def index_to_move(self, player, index):
    p1, p2 = _moves[index]
    return Move(player, p1, p2)

class Move(object):
    def __init__(self, player, p1, p2):
        self.__player = player

        if p2 < p1:
            self.__p1 = p2
            self.__p2 = p1
        else:
            self.__p1 = p1
            self.__p2 = p2

    def __eq__(self, other):
        if not isinstance(other, Move):
            raise RuntimeError('Move object and {} can not be compared'.format(other))

        return self.__p1 == other.__p1 and self.__p2 == other.__p2

    def execute(self, board_array):
        for x, y in self.__line_indices():
            board_array[y][x] = self.__player

    def validate(self, board_array):
        for x, y in self.__line_indices():
            if board_array[y][x] is not None:
                raise RuntimeError('There has already been moves or a part of them')

    def __line_indices(self):
        if self.__p1.x == self.__p2.x:
            return [(self.__p1.x, y) for y in range(self.__p1.y, self.__p2.y + 1)]

        if self.__p1.y == self.__p2.y:
            return [(x, self.__p1.y) for x in range(self.__p1.x, self.__p2.x + 1)]

        if self.__p2.x - self.__p1.x == self.__p2.y - self.__p1.y:
            x, y = self.__p1.x, self.__p1.y
            return [(x + d, y + d) for d in range(self.__p2.x - self.__p1.x + 1)]

        raise RuntimeError('Invalid points of move')
