import lastone
from lastone.point import Point

_positions = [(x, y) for y in range(lastone.BOARD_SIZE) for x in range(y + 1)]
_all_moves = [set([(x1, y1), (x2, y2)]) for x1, y1 in _positions for x2, y2 in _positions]
_raw_moves = []
for move in _all_moves:
    if not move in _raw_moves:
        _raw_moves.append(move)

_moves = []
for move in _raw_moves:
    move = list(move)
    if len(move) == 1:
        x, y = move[0]
        move = (Point(x, y), Point(x, y))
    else:
        x1, y1 = move[0]
        x2, y2 = move[1]

        if x2 - x1 == y2 - y1 or x1 == x2 or y1 == y2:
            move = (Point(x1, y1), Point(x2, y2))
        else:
            move = None

    if move is not None:
        _moves.append(move)

def action_to_move(player, index):
    p1, p2 = _moves[index]
    return Move(player, p1, p2)

class Move(object):
    def __init__(self, player, p1, p2):
        self.__player = player

        if p2.x < p1.x or p2.y < p1.y:
            self.__p1 = p2
            self.__p2 = p1
        else:
            self.__p1 = p1
            self.__p2 = p2

    def equals(self, other):
        if not isinstance(other, Move):
            raise RuntimeError('Move object and {} can not be compared'.format(other))

        if self.__p1 == other.__p1 and self.__p2 == other.__p2:
            return True

        if self.__p2 == other.__p1 and self.__p1 == other.__p2:
            return True

        return False

    def __hash__(self):
        return int('{}{}{}{}'.format(self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y))

    def __str__(self):
        return '{} -> {}'.format(self.__p1, self.__p2)

    __repr__ = __str__

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
