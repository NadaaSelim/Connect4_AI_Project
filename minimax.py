
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
   
    #bd.print_board(board)
    valid_locations=bd.get_valid_locations(board)
    if depth == 0 or is_terminal(board):
        if(is_terminal(board)):
            return None,utility(board)
        else:
            #print("end: ",ev.evaluate(board, maxPlayer))
            if maxPlayer == True:
                piece = AI_PIECE
            else:
                piece = PLAYER_PIECE
            return None, ev.evaluate(board, piece)
    if maxPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,AI_PIECE)
            new_value = minimax(board_copy,depth-1,False)[1]
            if new_value > value:
                value  = new_value
                column = col
                #print("val: ", value, "col: ", column)
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,PLAYER_PIECE)
            new_value = minimax(board_copy,depth-1,True)[1]
            if new_value < value:
                value  = new_value
                column = col
                #print("val: ", value, "col: ", column)
        return column, value
    
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


  
 

    





  





