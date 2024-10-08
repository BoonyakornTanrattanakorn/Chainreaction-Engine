
# Game state.
# Should be as small as possible.
class Board():
    def __init__(self, height, width, player_list):
        self.board = [[Tile() for j in range(width)] for i in range(height)]
        self.player_list = player_list
        self.player_value = dict([('-', 0)] + [(e.color, 0) for e in self.player_list])
        self.current_player = 0
        self.turn = 0

    def getPlayerValue(self, player):
        if self.turn == 0:
            return 0
        return self.player_value[player.color]
    
    def getCurrentPlayer(self):
        return self.player_list[self.current_player]
    
    def nextPlayer(self):
        self.current_player += 1
        if self.current_player >= len(self.player_list):
            self.current_player = 0

    # Attributes
    def __getitem__(self, idx):
        return self.board[idx]
    
    def __setitem__(self, idx, val):
        self.board[idx] = val
    
    def __str__(self):
        return '  ' + ' '.join([str(e).rjust(2) for e in range(len(self.board[0]))]) + '\n' + \
                '\n'.join([str(i).rjust(2) + ' ' + ' '.join([str(e) for e in self.board[i]]) for i in range(len(self.board))])
    
    def __len__(self):
        return len(self.board)
        

# Hold color and value of a tile.
class Tile():
    def __init__(self, color='-', value=0):
        self.color = color
        self.value = value
    
    def __str__(self):
        return str(self.color)+str(self.value)