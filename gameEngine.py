import Board

# This should handle the game logic. Takes a board (gamestate) as an input and does operation on it.
class gameEngine():
    def __init__(self):
        pass

    # Check if (Player) player is the winner in (Board) board. Returns boolean.
    def isWinner(self, player, board):
        if board.turn == 0:
            return False
        for row in board:
            for tile in row:
                if tile.color == '-' or tile.color == player.color:
                    continue
                else:
                    return False
        return True
    
    # (Player) player, (Board) board, move is a tuple (row, col)
    def playMove(self, player, move, board):
        if board.turn == 0:
            board[move[0]][move[1]].color = player.color
            board[move[0]][move[1]].value = 3
        else:
            self.chainReaction(player, move, board)

    def chainReaction(self, player, move, board):
        if move[0] < 0 or move[1] < 0 or move[0] >= len(board) or move[1] >= len(board[0]):
            return
        board[move[0]][move[1]].color = player.color
        board[move[0]][move[1]].value += 1
        if board[move[0]][move[1]].value == 4:
            board[move[0]][move[1]].value = 0
            board[move[0]][move[1]].color = '-'
            self.chainReaction(player, (move[0]+1, move[1]), board)
            self.chainReaction(player, (move[0]-1, move[1]), board)
            self.chainReaction(player, (move[0], move[1]+1), board)
            self.chainReaction(player, (move[0], move[1]-1), board)
        
        
