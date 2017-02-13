from lastone.board import Board

class Game(object):

    def __init__(self, first_player, second_player):
        self.__first_player = first_player
        self.__second_player = second_player

    def run(self, board=Board()):
        try:
            for player in self.__turns():
                print('Turn of {}'.format(player.name))
                move = None
                while move is None:
                    try:
                        move = player.select_move()
                        move.validate(board.asarray())
                    except Exception as e:
                        if player.debug_error:
                            print(e)
                        move = None

                board.append_move(move)
                board.show()
                if board.empty_count() == 1:
                    return player

        except KeyboardInterrupt:
            print('\n\nexit Game of Last One!')
            exit()

    def __turns(self):
        while True:
            yield self.__first_player
            yield self.__second_player
