import chess
from math import inf
import sys
from time import sleep

#ham fekri ba yazdan seyedi
class MinimaxKhafanAI():
    def __init__(self, depth):
        self.depth = depth
        self.isMaxinmizing = True
        self.actionList = ["first", "second", "third", "forth"]
        self.alpha = -sys.maxsize
        self.beta = sys.maxsize
        self.Plist = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 
                     1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
                     0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, 
                     0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 
                     0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5, 
                     0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, 
                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.Blist = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, 
                     -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
                     -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
                     -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
                     -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
                     -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
                     -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
                     -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        self.Qlist = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0, 
                     -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
                     -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
                     -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
                     0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5, 
                     -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0, 
                     -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0, 
                     -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        self.Klist = [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0,
                      -3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0,
                      -3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0,
                      -3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0,
                      -2.0,-3.0,-3.0,-4.0,-4.0,-3.0,-3.0,-2.0,
                      -1.0,-2.0,-2.0,-2.0,-2.0,-2.0,-2.0,-1.0,
                       2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
                       2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
        self.Rlist = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
                     -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5,
                     -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5,
                     -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5,
                     -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5,
                     -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5,
                      0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
        self.Hlist = [-5.0,-4.0,-3.0,-3.0,-3.0,-4.0,-4.0,-5.0,
                      -4.0,-2.0, 0.0, 0.0, 0.0, 0.0,-2.0,-4.0,
                      -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0,-3.0,
                      -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5,-3.0,
                      -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0,-3.0,
                      -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5,-3.0,
                      -4.0,-2.0, 0.0, 0.5, 0.5, 0.0,-2.0,-4.0,
                      -5.0,-4.0,-3.0,-3.0,-3.0,-3.0,-4.0,-5.0]
        


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
                evaluation += self.getPieceValue(str(board.piece_at(i)), x, i)
            else:
                evaluation -= self.getPieceValue(str(board.piece_at(i)), x, i)
        return evaluation

    def getPieceValue(self, piece, color, index):
        value = 0
        if(piece == None):
            return 0
        elif not color:
            if piece == "P" or piece == "p":
                value = self.Plist[index]
            if piece == "N" or piece == "n":
                value = self.Hlist[index]
            if piece == "B" or piece == "b":
                value = self.Blist[index]
            if piece == "R" or piece == "r":
                value = self.Rlist[index]
            if piece == "Q" or piece == "q":
                value = self.Qlist[index]
            if piece == 'K' or piece == 'k':
                value = self.Klist[index]
        elif color:
            index = 63 - index
            if piece == "P" or piece == "p":
                value = self.Plist[index]
            if piece == "N" or piece == "n":
                value = self.Hlist[index]
            if piece == "B" or piece == "b":
                value = self.Blist[index]
            if piece == "R" or piece == "r":
                value = self.Rlist[index]
            if piece == "Q" or piece == "q":
                value = self.Qlist[index]
            if piece == 'K' or piece == 'k':
                value = self.Klist[index]
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