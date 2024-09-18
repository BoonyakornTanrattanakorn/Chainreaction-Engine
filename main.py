import Board
import Player
import gameEngine
from time import sleep
import os

wins = dict({'r':0, 'b':0})
while True:
    game = gameEngine.gameEngine()
    player_list = [Player.randomBot('r'), Player.oneDepthMaxScoreBot('b')]
    board = Board.Board(5, 5, player_list)
    isRunning = True
    while isRunning:
        for i in range(len(player_list)):
            print(f"Current turn: {board.turn}")
            print(f"It is player '{board.getCurrentPlayer().color}' turn.")
            print("Score:")
            for p in board.player_list:
                print(f"{p.color} : {board.getPlayerValue(p)}")
            print("Wins:")
            for p in board.player_list:
                print(f"{p.color} : {wins[p.color]}")
            print(board)
            move = board.getCurrentPlayer().generateMove(board)
            game.playMove(board.getCurrentPlayer(), move, board)
            if game.isWinner(board.getCurrentPlayer(), board):
                os.system('cls')
                print(board)
                print(f"{board.turn} turns has elapsed! The game is over! Player '{board.getCurrentPlayer().color}' has won!")
                wins[board.getCurrentPlayer().color] += 1
                isRunning = False
                break
            board.nextPlayer()
            sleep(0)
            os.system('cls')
        board.turn += 1

