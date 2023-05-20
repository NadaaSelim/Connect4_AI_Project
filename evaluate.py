import board as bd
import copy
import numpy as np 


ROW_COUNT = 6   #number of rows in connect 4
COLUMN_COUNT = 7   #number of columns in connect 4


# function that evaluates the score for a list made up of 4 pieces that
# can be horizontal, vertical or diagonal
def list_score(pieces_list, piece, opp_piece):
    score = 0
    # means the player won so score increases and is less of an increase
    # compared to blocking opponent from winning because because blocking is more important
    if(pieces_list.count(piece)==4):    
        score += 1000000
    
    if(pieces_list.count(opp_piece)==4):    #means the opponent won so score decreases
        score -= 100000000
    else:
        # if the opponent didn't win then for every piece for that player it gets 25 points
        score += pieces_list.count(piece) * 25     
        # and if the number of opponent pieces is 3 so they are about to win the player will get 
        # a score increase if it blocks that win using one of its pieces 
        if(pieces_list.count(opp_piece) == 3 and pieces_list.count(piece) == 1):
            score += 100000000
        # or if it didn't block it and instead there is a zero so opponent can win
        # the score will be decreased greatly
        elif(pieces_list.count(opp_piece) == 3 and pieces_list.count(0) == 1):
            score -= 100000000
    return score

# function that given a board uses the list_score function to evaluate every 4 pieces in it 
# along the 4 directions: horizontal, vertical, diagonal, anti-diagonal
def evaluate(board, piece):

        # deciding who is the opponent
        if(piece == 1):
            opp_piece = 2
        else:
            opp_piece = 1
        score = 0
        
        # loop for rewarding boards with pieces that are closer to the center so that whenever
        # two states are identical the agent chooses the one that is nearer to the center since it
        # has more possible moves and wins
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
        # loop to score every 4 pieces horizontally
        for r in range(ROW_COUNT):
            for j in range(COLUMN_COUNT-3):
                # splits every row to 4 pieces and then moves the split by one piece
                pieces_list = board[r][j:j+4].tolist()  
                score += list_score(pieces_list, piece, opp_piece)
                
                
        # loop to score every 4 pieces vertically
        for r in range(COLUMN_COUNT):
            for j in range(ROW_COUNT-3):
                # splits every column to 4 pieces and then moves the split by one piece
                pieces_list = board[:,r].tolist()
                pieces_list = pieces_list[j:j+4]
                score += list_score(pieces_list, piece, opp_piece)
        
        # loop to score every 4 pieces in the anti-diagonal direction x = -y
        for d in range(-2, 4):
             # gets the diagonal staring with diagonals that are 4 pieces in length 
            diagonal = board.diagonal(d).tolist()
            for i in range(0, len(diagonal)-3):
                # splits the diagonal to 4 pieces and then moves the split by one piece every time
                pieces_list = diagonal[i:i+4]
                score += list_score(pieces_list, piece, opp_piece)
                
        # loop to score every 4 pieces in the diagonal direction x = y
        for d in range(-2, 4):
            # gets the diagonal staring with diagonals that are 4 pieces in length 
            diagonal = np.fliplr(board).diagonal(d).tolist()
            for i in range(0, len(diagonal)-3):
                # splits the diagonal to 4 pieces and then moves the split by one piece every time
                pieces_list = diagonal[i:i+4]
                score += list_score(pieces_list, piece, opp_piece)
        return score
    
