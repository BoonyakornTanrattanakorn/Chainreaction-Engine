class Game():
    def __init__(self):
        self.height = 5
        self.width = 5
        self.board = [[('-',0) for j in range(self.width)] for i in range(self.height)]
        self.colors = ['r', 'b']

    def checkWinner(self):
        dead_color = self.colors[:]
        for row in self.board:
            for i in row:
                if i[0] in dead_color:
                    dead_color.remove(i[0])
                    if dead_color == []:
                        return ''
        return [e for e in self.colors if e not in dead_color][0]

    def firstTurn(self):
        for color in self.colors:
            i, j = self.takeFirstInput(color)
            self.board[i][j] = (color, 3)
            self.printBoard()

    def play(self, color):
        i, j = self.takeInput(color)
        self.reaction(i, j, color)
    
    def reaction(self, i, j, color):
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        self.board[i][j] = (color, self.board[i][j][1] + 1)
        if self.board[i][j][1] == 4:
            self.board[i][j] = ('-', 0)
            self.reaction(i+1, j, color)
            self.reaction(i-1, j, color)
            self.reaction(i, j+1, color)
            self.reaction(i, j-1, color)
        

    def takeFirstInput(self, color):
        while True:
            [i, j] = [int(e) for e in input(f"Input (row col) for player {color}: ").strip().split(' ')]
            if i < 0 or j < 0 or i >= self.height or j >= self.width:
                print("Coordinates out of bound!")
            elif self.board[i][j][0] != '-':
                print("Tile already taken!")
            else:
                return i, j
            
    def takeInput(self, color):
        while True:
            [i, j] = [int(e) for e in input(f"Input (row col) for player {color}: ").strip().split(' ')]
            if i < 0 or j < 0 or i >= self.height or j >= self.width:
                print("Coordinates out of bound!")
            elif self.board[i][j][0] != color:
                print("Not your tile!")
            else:
                return i, j

    def printBoard(self):
        print('  ' + ' '.join([str(e).rjust(2) for e in range(self.width)]))
        for i in range(self.height):
            print(str(i) + ' ' + ' '.join([f"{e[0]}{e[1]}" for e in self.board[i]]))


if __name__ == "__main__":
    game = Game()