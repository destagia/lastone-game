# -*- coding: utf-8 -*-

import lastone
import numpy as np

class Board(object):

    def __init__(self):
        self.__moves = []
        self.__cache_id = -1
        self.__cache_array = None

    def append_move(self, move):
        self.__moves.append(move)

    def __id(self):
        return len(self.__moves)

    def asarray(self):
        cache_id = self.__id()
        if self.__cache_id != cache_id:
            self.__cache_id = cache_id
            self.__cache_array = [[None for _ in range(y + 1)] for y in range(lastone.BOARD_SIZE)]
            for move in self.__moves:
                move.execute(self.__cache_array)

        return self.__cache_array

    def empty_count(self):
        count = 0
        for row in self.asarray():
            for point in row:
                if point is None:
                    count += 1
        return count

    def show(self):
        print('')
        row_index = 0
        for row in self.asarray():
            line = ''
            for _ in range(0, (lastone.BOARD_SIZE - 1 - row_index)):
                line += '  '
            for player in row:
                if player == None:
                    line += '|'
                else:
                    line += '✗'
                line += '   '
            print(line)
            row_index += 1
        print('')
