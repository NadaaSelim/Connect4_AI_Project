import board as bd
import copy
import numpy as np 


ROW_COUNT = 6   #number of rows in connect 4
COLUMN_COUNT = 7   #number of columns in connect 4



def list_score(pieces_list, piece, opp_piece):
    score = 0
    if(pieces_list.count(piece)==4):
        score += 1000000
    
    if(pieces_list.count(opp_piece)==4):
        score -= 100000000
    else:
        score += pieces_list.count(piece) * 25
        #score -= pieces_list.count(opp_piece) * 25
        if(pieces_list.count(opp_piece) == 3 and pieces_list.count(piece) == 1):
            score += 100000000
        elif(pieces_list.count(opp_piece) == 3 and pieces_list.count(0) == 1):
            score -= 100000000
    return score

def evaluate(board, piece):

        if(piece == 1):
            opp_piece = 2
        else:
            opp_piece = 1
        score = 0
        
        for r in range(COLUMN_COUNT):
            column = board[:,r].tolist()
            column_count = column.count(piece)
            if(abs(3-column_count) == 0):
                score += 100
            elif(abs(3-column_count) == 1):
                score += 70
            elif(abs(3-column_count) == 2):
                score += 50
            else:
                score += 10
        # horizontal
        for r in range(ROW_COUNT):
            for j in range(COLUMN_COUNT-3):
                pieces_list = board[r][j:j+4].tolist()
                score += list_score(pieces_list, piece, opp_piece)
                
                
        # vertical
        for r in range(COLUMN_COUNT):
            for j in range(ROW_COUNT-3):
                pieces_list = board[:,r].tolist()
                pieces_list = pieces_list[j:j+4]
                score += list_score(pieces_list, piece, opp_piece)
        
        # anti-diagonal
        for d in range(-2, 4):
            diagonal = board.diagonal(d).tolist()
            for i in range(0, len(diagonal)-3):
                pieces_list = diagonal[i:i+4]
                score += list_score(pieces_list, piece, opp_piece)
                
        # diagonal
        for d in range(-2, 4):
            diagonal = np.fliplr(board).diagonal(d).tolist()
            for i in range(0, len(diagonal)-3):
                pieces_list = diagonal[i:i+4]
                score += list_score(pieces_list, piece, opp_piece)
        return score
    
# todo remove this             
board = np.array([  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 2, 1, 2]
                                                ])
print(evaluate(board,2))