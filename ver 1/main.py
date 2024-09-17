import gameEngine
from time import time

#start_t = time()

Game = gameEngine.Game()
Game.printBoard()
Game.firstTurn()
[i, j] = [int(e) for e in input(f"Input (row col) for player {color}: ").strip().split(' ')]
isRunning = True
while isRunning:
    for color in Game.colors:
        Game.play(color)
        Game.printBoard()
        winner = Game.checkWinner()
        if winner:
            print(f"The game is over! The winner is: {winner}!")
            isRunning = False
            break


#print(f"Run time: {time()-start_t} seconds!")
