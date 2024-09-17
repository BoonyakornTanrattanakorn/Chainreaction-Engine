import secrets

class randomPlayer():
    def __init__(self, color):
        self.color = color

    def availableMoves(self, board):
        moves = []
        for i in len(board):
            for j in len(board[0]):
                if board[i][j][0] == self.color:
                    moves.append((i, j))
        return moves
    
    def chooseRandomMove(self, moves):
        move = secrets.choice(moves)
        return move[0], move[1]