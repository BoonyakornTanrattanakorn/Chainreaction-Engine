import secrets
import gameEngine

class Player():
    def __init__(self, color):
        self.color = color

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
    

# Choose a random move
class randomBot(Player):
    def __init__(self, color):
        super().__init__(color)

    def generateMove(self, board):
        return secrets.choice(self.generateAllMoves(board))

    def generateAllMoves(self, board):
        if board.turn == 0:
            return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j].color == '-']
        else:
            return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j].color == self.color]
        

class minimaxBot(Player):
    def __init__(self, color):
        super().__init__(color)
        self.game = gameEngine.gameEngine()

    def generateMove(self, board):
        time_limit = 10
        depth = 0
        moves = [[e, []]]
        while True:
            break
            prev_moves = moves[-2]
            next_moves = moves[-1]
            for move in prev_moves:
                pass
            
    def generateAllMoves(self, board):
        if board.turn == 0:
            return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j].color == '-']
        else:
            return [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j].color == self.color]