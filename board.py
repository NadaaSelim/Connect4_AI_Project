import numpy as np
import pygame
import random

ROW_COUNT = 6   #number of rows in connect 4
COLUMN_COUNT = 7   #number of columns in connect 4

# Function that creates the board
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)     # creates a matrix and initializes all cells by zero
    return board

# Function that checks if a certain column is valid for adding a piece
def is_valid_column(board, column):
    # checks to see if the board at the top most row [5] at the specified column free or not
    is_valid = board[ROW_COUNT-1][column] == 0
    return is_valid
    
# Function that adds a piece in it's correct position if possible
def add_piece(board, column, player_num):
        for i in range(ROW_COUNT):      # loops over all rows at specified column until it finds an empty cell
            if board[i][column] == 0:
                board[i][column] = player_num
                break
  
# Function that prints a board in its correct connect4 orientation  
def print_board(board):   
    print(np.flip(board, 0))   #flips the matrix around the x axis
    
# Function that checks if a player won after every move
def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            # Check horizontal and positively sloped diagonals
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ) or (
                r < ROW_COUNT - 3
                and board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            # Check vertical and negatively sloped diagonals
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ) or (
                r >= 3
                and board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True

    return False