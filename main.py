import Board
import Player
import gameEngine
from time import sleep
import os

game = gameEngine.gameEngine()
board = Board.Board(5, 5)
players = [Player.Player('r'), Player.randomBot('b')]
isRunning = True
while isRunning:
    for player in players:
        print(f"Current turn: {board.turn}")
        print(f"It is player '{player.color}' turn.")
        print("Score:")
        for p in players:
            print(f"{p.color} : {board.getPlayerValue(p)}")
        print(board)
        move = player.generateMove(board)
        game.playMove(player, move, board)
        if game.isWinner(player, board):
            print(board)
            print(f"{board.turn} turns has elapsed! The game is over! Player '{player.color}' has won!")
            isRunning = False
            break
        sleep(0.5)
        os.system('cls')
    board.turn += 1

