
import random
import board as bd
import copy
import numpy as np
import evaluate as ev
import math


PLAYER_PIECE=1  # min
AI_PIECE=2  #max


def utility(board):
    if(bd.get_winner(board,AI_PIECE) ):
        return 10000000000   #max won
    if(bd.get_winner(board,PLAYER_PIECE) ):
        return -10000000000   #min won
    else:
        return 0    #tie


def is_terminal(board):
    return bd.get_winner(board,PLAYER_PIECE) or bd.get_winner(board,AI_PIECE) or len(bd.get_valid_locations(board)) == 0

def minimax(board,depth,maxPlayer):
   
    # gets all possible valid loactions that the player can add a piece in
    valid_locations=bd.get_valid_locations(board)
    # stopping condition 
    # 1- reached required depth
    # 2-state is a terminal state (win , lose ,tie)
    if depth == 0 or is_terminal(board):
        if(is_terminal(board)):
            return None,utility(board)
        else:
            # evaluates the current board score based on player's turn
            if maxPlayer == True:
                piece = AI_PIECE
            else:
                piece = PLAYER_PIECE
            return None, ev.evaluate(board, piece)
    
    # maxmizing  palyer turn
    # finds the move the leads to the most possible wins
    if maxPlayer:
        
        # intialize
        score = -math.inf
        column = random.choice(valid_locations)

        # tries every possible move
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,AI_PIECE)
            new_score = minimax(board_copy,depth-1,False)[1]

            # takes the max move (best move)
            if new_score > score:

                score  = new_score
                column = col
        
        return column, score
    
    #minimize player's turn
    #finds the move that lead to lowest number of wins for the max player
    else:

        #intialize
        score = math.inf
        column = random.choice(valid_locations)

        # tries every possible move
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,PLAYER_PIECE)
            new_score = minimax(board_copy,depth-1,True)[1]

            # takes the min score
            if new_score < score:

                score  = new_score
                column = col
               
        return column, score
    
def alpha_beta(board,alpha,beta,depth,maxPlayer):
    valid_locations=bd.get_valid_locations(board)
    if depth == 0 or is_terminal(board):
        #bd.print_board(board)
        if(is_terminal(board)):
            #print(utility(board))
            return None,utility(board)
        else:
            #print(evaluate_board(board,maxPlayer))
            if maxPlayer == True:
                piece = AI_PIECE
            else:
                piece = PLAYER_PIECE
            return None,ev.evaluate(board, maxPlayer)
    if maxPlayer:
        value=-math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,AI_PIECE)
            new_value = alpha_beta(board_copy,alpha,beta,depth-1,False)[1]
            if new_value > value:
                value  = new_value
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        #return column, value
    else:
        value=math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,PLAYER_PIECE)
            new_value = alpha_beta(board_copy,alpha,beta,depth-1,True)[1]
            if new_value < value:
                value  = new_value
                column = col
            beta = min(beta,value)
            if alpha >= beta:
                break
        #return column, value
    return column ,value



# todo reemove
board = np.array([  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 2, 2, 0, 0],
                    [0, 0, 0, 2, 1, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0]
                                                ])

#print(evaluate_board(board,2))


  
 

    





  





