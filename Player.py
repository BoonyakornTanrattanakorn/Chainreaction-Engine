import secrets
import concurrent.futures
import time
import copy
import gameEngine

class Player():
    def __init__(self, color):
        self.color = color
        self.value = 0

    # Takes input
    def generateMove(self, board):
        while True:
            move = input("Input moves (row col): ").strip().split(' ')
            if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
                move[0], move[1] = int(move[0]), int(move[1])
                if self.isValidMove(move[0], move[1], board):
                    return (move[0], move[1])
            print("Invalid input.")
    
    # Check if move is valid. Returns boolean.
    def isValidMove(self, row, col, board):
        # Check out of bound
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            print("Selected tile is out of bound.")
            return False
        if board.turn == 0:
            if board[row][col].color != '-':
                print("Selected tile is not empty.")
                return False
        else:
            if board[row][col].color != self.color:
                print("Selected tile is not your own.")
                return False
        return True
    
    def generateAllMoves(self, board):
        if board.turn == 0:
            return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j].color == '-']
        else:
            return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j].color == self.color]
    

# Always choose a random move
class randomBot(Player):
    def __init__(self, color):
        super().__init__(color)

    def generateMove(self, board):
        return secrets.choice(self.generateAllMoves(board))
        

# Always choose move that maximize own score and minimize others score. Only search one depth. If there are several equal-scoring moves then choose random.
class oneDepthMaxScoreBot(Player):
    def __init__(self, color):
        super().__init__(color)
        self.game = gameEngine.gameEngine()

    def generateMove(self, board):
        moves = self.generateAllMoves(board)
        max_score = - 10 ** 9
        for move in moves:
            move_value = self.moveValue(move, board, self)
            if move_value < max_score:
                continue
            elif move_value == max_score:
                max_score_moves.append(move)
            else:
                max_score = move_value
                max_score_moves = [move]
        return secrets.choice(max_score_moves)

    def moveValue(self, move, board, player):
        next_board = copy.deepcopy(board)
        self.game.playMove(self, move, next_board)
        value = 0
        for p in board.player_list:
            if p == player:
                value += next_board.getPlayerValue(p) - board.getPlayerValue(p)
            else:
                value += board.getPlayerValue(p) - next_board.getPlayerValue(p)
        return value