import sys

import numpy as np


# 0->empty, 1->X 2->O
def make_board():
    return np.zeros((3, 3), int)


def preamble():
    print("Enter the turn in this format(zero-indexed): x,y")
    print("Eg. to play on the 1st row, 2nd column, enter 0,1")


def put_on_board(board, where, what):
    board[where[0], where[1]] = what


def pc_turn(board):
    vacancies = get_vacant(board)
    r = np.random.randint(0, len(vacancies))
    return vacancies[r]


def user_turn(board, user):
    peice = "X"
    if user == 2:
        peice = "O"

    print("your turn")
    print(board_ui(board))
    ugh = input("Where to play?(You are playing {})\n".format(peice))
    ugh.replace(" ", "")
    x, y = ugh.split(",")
    vacancies = get_vacant(board)
    play = [int(x), int(y)]
    if not vacancies.__contains__(play):
        idiot = True
        while idiot:
            print("Play somewhere else.")
            ugh = input()
            ugh.replace(" ", "")
            x, y = ugh.split(",")
            play = [int(x), int(y)]
            if vacancies.__contains__(play):
                idiot = False
    return play


def board_ui(board):
    ui = "-------------------\n"
    for i in range(3):
        ui += "\t |"
        for j in range(3):
            if board[i, j] == 0:
                ui += " "
            if board[i, j] == 1:
                ui += "X"
            if board[i, j] == 2:
                ui += "O"
            if j != 2:
                ui += "  "
        ui += "| \n"
    ui += "-------------------"
    return ui


def game_is_over(board):
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] and board[i, 0] != 0:
            return True
        if board[0, i] == board[1, i] == board[2, i] and board[0, i] != 0:
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] and board[1, 1] != 0:
        return True
    if board[2, 0] == board[1, 1] == board[0, 2] and board[1, 1] != 0:
        return True
    return False


def get_vacant(board):
    vacancies = []
    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:
                vacancies.append([i, j])
    return vacancies


def get_winner(board, user):
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] and board[i, 0] == user:
            return True
        if board[0, i] == board[1, i] == board[2, i] and board[0, i] == user:
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] and board[1, 1] == user:
        return True
    if board[2, 0] == board[1, 1] == board[0, 2] and board[1, 1] == user:
        return True
    return False


def evaluate(board):
    evaluation = 8
    return evaluation


def calc_crosses(board):
    count = 8
    return count


def calc_noughts(board):
    count =8
    return count

