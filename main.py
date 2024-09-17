import Board
import Player
import gameEngine
from time import sleep
import os

while True:
    game = gameEngine.gameEngine()
    board = Board.Board(5, 5)
    players = [Player.randomBot('r'), Player.randomBot('b')]
    isRunning = True
    while isRunning:
        for player in players:
            print(f"Current turn: {board.turn}")
            print(f"It is player '{player.color}' turn.")
            print(board)
            move = player.generateMove(board)
            game.playMove(player, move, board)
            sleep(0.2)
            os.system('cls')
            if game.isWinner(player, board):
                print(board)
                print(f"{board.turn} turns has elapsed! The game is over! Player '{player.color}' has won!")
                isRunning = False
                sleep(5)
                break

        board.turn += 1
