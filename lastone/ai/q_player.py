from lastone.ai.q_network import QNetwork
from lastone.move import action_to_move
import random

class QPlayer(object):
    debug_error = False

    def __init__(self, board):
        self.name = 'Q-chan'
        self.__board = board
        self.__network = QNetwork()

    @property
    def xp(self):
        return self.__network.xp

    def select_move(self):
        state = self.xp.zeros((2, 5, 5), dtype=self.xp.float32)
        board_array = self.__board.asarray()
        for i in range(len(board_array)):
            row = board_array[i]
            for j in range(len(row)):
                point = row[j]
                if point == self:
                    state[0][i][j] = 1.0
                elif point is not None:
                    state[1][i][j] = 1.0

        if random.uniform(0, 1) > 0.1:
            action = random.choice(range(75))
        else:
            q_values = self.__network(state.reshape(1, 2, 5, 5))
            action = self.xp.argmax(q_values.data)

        move = action_to_move(self, int(action))
        return move