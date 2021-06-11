import random
from time import sleep
import chess

class RandomAI():
    def init(self):
        pass

    def choose_move(self, board):
        moves = list(board.legal_moves)
        move = random.choice(moves)
        sleep(1)
        print("Random AI recommending move " + str(move))
        return move