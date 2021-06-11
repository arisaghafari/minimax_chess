import chess
from math import inf
import sys
from time import sleep

#ham fekri ba yazdan seyedi
class AlphaBetaAI():
    def __init__(self, depth):
        self.depth = depth
        self.isMaxinmizing = True
        self.actionList = ["first", "second", "third", "forth"]
        self.alpha = -sys.maxsize
        self.beta = sys.maxsize

    def choose_move(self, board):
        alpha = self.alpha
        beta = self.beta
        actionList = self.actionList
        isMaximizing = self.isMaxinmizing
        depth = self.depth
        moves = board.legal_moves
        bestMove = -sys.maxsize
        bestMoveFinal = None
        tempAction = []
        for i in range(len(actionList) - 4, len(actionList)):
            tempAction.append(actionList[i])
        for x in moves:
            move = chess.Move.from_uci(str(x))
            if not (move in tempAction):
                board.push(move)
                value = max(bestMove, self.miniMax(board, depth - 1, not isMaximizing, alpha, beta))
                board.pop()
                if( value > bestMove):
                    #print("Best score: " ,str(bestMove))
                    bestMove = value
                    bestMoveFinal = move
        sleep(1)
        actionList.append(bestMoveFinal)
        return bestMoveFinal

    def miniMax(self, board, depth, maximizingPlayer, alpha, beta):
        actionList = self.actionList
        if depth == 0 or board.is_game_over():
            return -self.evaluation(board)
        moves = board.legal_moves
        tempAction = []
        for i in range(len(actionList) - 4, len(actionList)):
            tempAction.append(actionList[i])
        if maximizingPlayer:
            value = -sys.maxsize
            for move in moves:
                if not(move in tempAction):
                    temp = chess.Move.from_uci(str(move))
                    board.push(temp)
                    value = max(value, self.miniMax(board, depth - 1, False, alpha, beta))
                    board.pop()
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        return value
            return value
        else:
            value = sys.maxsize
            for move in moves:
                if not(move in tempAction):
                    temp = chess.Move.from_uci(str(move))
                    board.push(temp)
                    value = min(value, self.miniMax(board, depth - 1, True, alpha, beta))
                    board.pop()
                    beta = min(beta, value)
                    if alpha >= beta:
                        return value
            return value

    def evaluation(self, board):
        i = 0
        evaluation = 0
        x = True
        try:
            x = bool(board.piece_at(i).color)
        except AttributeError as e:
            x = x
        while i < 63:
            i += 1
            if x:
                evaluation += self.getPieceValue(str(board.piece_at(i)))
            else:
                evaluation -= self.getPieceValue(str(board.piece_at(i)))
        return evaluation

    def getPieceValue(self, piece):
        if(piece == None):
            return 0
        value = 0
        if piece == "P" or piece == "p":
            value = 10
        if piece == "N" or piece == "n":
            value = 30
        if piece == "B" or piece == "b":
            value = 30
        if piece == "R" or piece == "r":
            value = 50
        if piece == "Q" or piece == "q":
            value = 90
        if piece == 'K' or piece == 'k':
            value = 900
        return value
    
    def letterToNumber(self, letter):
        if letter[0] == 'a' or letter[0] == 'A':
            i = 0
        elif letter[0] == 'b' or letter[0] == 'B':
            i = 1
        elif letter[0] == 'c' or letter[0] == 'C':
            i = 2
        elif letter[0] == 'd' or letter[0] == 'D':
            i = 3
        elif letter[0] == 'e' or letter[0] == 'E':
            i = 4
        elif letter[0] == 'f' or letter[0] == 'F':
            i = 5
        elif letter[0] == 'g' or letter[0] == 'G':
            i = 6
        elif letter[0] == 'h' or letter[0] == 'H':
            i = 7
        num = 8 * (int(letter[1]) - 1) + i
        return num