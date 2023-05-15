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
                return i, column        # returns the position in which the piece was added as a tuple
  
# Function that prints a board in its correct connect4 orientation  
def print_board(board):   
    print(np.flip(board, 0))   #flips the matrix around the x axis
    
# Function that checks if a player won after every move
def winning_move(board, piece, last_row, last_col):
    
    # the (x,y) for every direction represent how I move in the board to check a win in that direction
    directions = [
        (0, 1),   # Horizontal so move along the x-axis, y = 0
        (1, 0),   # Vertical so move along the y-axis, x = 0
        (1, 1),   # Diagonal so move along the line x = y
        (-1, 1)   # Anti-Diagonal so move along the line x = -y or -x = y
    ]

    # every time this for loop iterates it checks for one of the directions starting from the last piece added
    for dr, dc in directions:
        count = 1      # because we have the last piece added then count = 1 and if it can reach 4 then it's a win
        r, c = last_row, last_col

        # Check in the positive direction
        while True:
            # adds the the values for the direction being checked to the position of the last piece
            # so we are moving along the line for each direction with every while loop iteration
            r += dr
            c += dc
            # and as long as the position we are checking
            # its row position between 0 and 6 and column position between 0 and 7 then we are within our board parameters
            # AND its holding a piece that matches the last added piece
            # Then continue and count of connected pieces is incremented by 1
            # else break the loop and enter the next while loop
            if not (0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT) or board[r][c] != piece:
                break

            count += 1

        r, c = last_row, last_col

        # Check in the negative direction, so it's along the same line for that direction just moves backward
        while True:
            r -= dr
            c -= dc
            # and as long as the position we are checking
            # its row position between 0 and 6 and column position between 0 and 7 then we are within our board parameters
            # AND its holding a piece that matches the last added piece
            # Then continue and count of connected pieces is incremented by 1
            # else break the loop 
            if not (0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT) or board[r][c] != piece:
                break

            count += 1
        # checks to see if count is 4 or more so we have connected 4 pieces and the player with these pieces won
        if count >= 4:
            return True
        # if not for loop executes another time to search along a different line or all direction are done so return false

    return False
