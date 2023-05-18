
import random
import board as bd
import copy
import numpy as np



PLAYER_PIECE=1  # min
AI_PIECE=2  #max


def horizontal(board,piece,streak):
    score = 0
    for i in range(bd.ROW_COUNT):
        count = 0
        for j in range(bd.COLUMN_COUNT):
            if(board[i][j] == piece):
                count += 1
            
            else:
                if(count >= streak):    # to take in consideration -> 1 1 1 1  is score 1 not 2
                    score += 1
                count = 0
                
    return score

def vertical(board,piece,streak):
    score = 0
    for i in range(bd.COLUMN_COUNT):
        count = 0
        for j in range(bd.ROW_COUNT):
            if(board[j][i] == piece ):
                count += 1
            else:
                if(count >= streak):    # to take in consideration -> 1 1 1 1  is score 1 not 2
                    score += 1
                count = 0  
        
    return score

def diagnoal_PAST(board,piece,streak):
    score = 0
    row = 0
    column = 0
    count=0
    while(row < bd.ROW_COUNT and column <bd.COLUMN_COUNT):
        if(board[row][column]==piece):
            count+=1
        else:
            if(count>=streak):
                score+=1
            count = 0
        row+=1 
        column+=1
    return score





def diagonals(board,piece,streak):
    score = 0
    n = len(board)
    diagonals = []  # upper-left-to-lower-right diagonals

    for p in range(2*n-1):
        diagonals.append([board[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])

    for i in range(len(diagonals)):
        print(diagonals[i])
    for i in range(len(diagonals)):
        count = 0
        for j in range (len(diagonals[i])):
            
                if(diagonals[i][j] == piece):
                    count +=1
                else:
                    if(count >= streak):
                        score+=1
                    count=0
    return score
        
          

# evaluate the current board (state) based on
# how many adjacent four pieces vertically ,horizontally,diagonally(poistive and negative sloped)
#the score of four pieces is 150 , the score of three is 50 , the score of 2 is 15, score of center columns is its weight * 10
def evaluate_board(board,maxPlayer):
    ai_center_score =0
    opp_center_score=0

    #realisticly ai should prefer the board with more of its pieces in center column as it would mean more chances to win
    for col in range(bd.COLUMN_COUNT):
        for row in range(bd.ROW_COUNT):
            if board[row][col] == AI_PIECE:
                 if col == bd.COLUMN_COUNT//2:
                     ai_center_score += 3
                 elif col in range(2,5):
                     ai_center_score+= 2
                 else:
                     ai_center_score +=1
            if board[row][col] == PLAYER_PIECE:
                 if col == bd.COLUMN_COUNT//2:
                     opp_center_score += 3
                 elif col in range(2,5):
                     opp_center_score+= 2
                 else:
                     opp_center_score +=1
    four_ai = 0 
    three_ai = 0
    two_ai = 0
    four_player = 0
    three_player = 0
    two_player = 0

    four_ai  += horizontal(board,AI_PIECE,4)
    three_ai  += horizontal(board,AI_PIECE,3)
    two_ai  += horizontal(board,AI_PIECE,2)

    four_ai  += vertical(board,AI_PIECE,4)
    three_ai  += vertical(board,AI_PIECE,3)
    two_ai  += vertical(board,AI_PIECE,2)

    four_player  += horizontal(board,PLAYER_PIECE,4)
    three_player  += horizontal(board,PLAYER_PIECE,3)
    two_player  += horizontal(board,PLAYER_PIECE,2)

    four_player  += vertical(board,PLAYER_PIECE,4)
    three_player  += vertical(board,PLAYER_PIECE,3)
    two_player  += vertical(board,PLAYER_PIECE,2)

    #return (four_ai * 500 + three_ai * 150 + two_ai * 50 + ai_center_score*10) - (four_player * 300 + three_player * 100 + two_player * 40 + opp_center_score*10)
    return (four_ai  + three_ai  + two_ai  + ai_center_score) - (four_player  + three_player  + two_player  + opp_center_score)

    #return (four_ai * 300 + three_ai * 150 + two_ai * 50 + ai_center_score*10) - (four_player * 300 + three_player * 150 + two_player * 50 + opp_center_score*10)
        
    
    



def utility(board):
    if(bd.get_winner(board,AI_PIECE) ):
        return 150   #max won
    if(bd.get_winner(board,PLAYER_PIECE) ):
        return -150   #min won
    else:
        return 0    #tie


def is_terminal(board):
    return bd.get_winner(board,PLAYER_PIECE) or bd.get_winner(board,AI_PIECE) or len(bd.get_valid_locations(board)) == 0

def minimax(board,depth,maxPlayer):
   
    valid_locations=bd.get_valid_locations(board)
    if depth == 0 or is_terminal(board):
        #bd.print_board(board)
        if(is_terminal(board)):
            print(utility(board))
            return None,utility(board)
        else:
            #print(evaluate_board(board,maxPlayer))
            return None,evaluate_board(board,maxPlayer)
    if maxPlayer:
        value=-1000000
        column = random.choice(valid_locations)
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,AI_PIECE)
            new_value = minimax(board_copy,depth-1,False)[1]
            if new_value > value:
                value  = new_value
                column = col
        return column, value
    else:
        value=1000000
        column = random.choice(valid_locations)
        for col in valid_locations:
            board_copy = copy.deepcopy(board)
            bd.add_piece(board_copy,col,PLAYER_PIECE)
            new_value = minimax(board_copy,depth-1,True)[1]
            if new_value < value:
                value  = new_value
                column = col
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
            return None,evaluate_board(board,maxPlayer)
    if maxPlayer:
        value=-1000000
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
                print("Pruning..")
                break

        #return column, value
    else:
        value=1000000
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
                print("Pruning..")
                break
        #return column, value
    return column ,value

def test():
    matrix= np.array([ [1, 0, 2, 0, 0, 2, 2],
                  [1, 1, 1, 2, 1, 2, 2],
                  [0, 0, 0, 0, 2, 2, 2],
                  [0, 0, 0, 0, 2, 0, 0],
                  [0, 0, 0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 0, 0, 2]
            ],np.int32)
    print(vertical(matrix,AI_PIECE,2))




  





