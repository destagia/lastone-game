from lastone.move import Move
from lastone.point import Point

class Player(object):
    def __init__(self, name):
        self.__name = name

    def select_move(self):
        move_str = raw_input('Please input move of {}: '.format(self.__name))
        p1, p2 = move_str.split(' ')
        y1, x1 = p1.split(',')
        y2, x2 = p2.split(',')
        return Move(self, Point(int(x1), int(y1)), Point(int(x2), int(y2)))