import random
import numpy as np

from week_1.tic_tac_toe.crosses_and_noughts import *

preamble()
board = make_board()
user = 1
pc = 2
turn = True
if np.random.rand() > 0.5:
    user = 2
    pc = 1
    turn = False

while not game_is_over(board):
    if turn:
        place = user_turn(board, user)
        put_on_board(board, place, user)
        turn = 0
    else:
        place = pc_turn(board)
        put_on_board(board, place, pc)
        turn = 1



winner = get_winner(board, user)
if winner:
    print("You Won!")
else:
    print("You Lost!")
