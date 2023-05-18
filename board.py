import numpy as np
import pygame
import random
import sys
import menu
SQUARESIZE = 100
WHITE = (255,255,255)
#BOARDCOLOR = (240,230,140)
BOARDCOLOR = (211,211,211)
RED = (128,0,0)
BLUE = (0,0,255)
screen = None
ROW_COUNT = 6   #number of rows in connect 4
COLUMN_COUNT = 7   #number of columns in connect 4
height = (ROW_COUNT+1) * SQUARESIZE         # added extra row for the top bar which holds the piece to be dropped
width = COLUMN_COUNT * SQUARESIZE

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
                #draw_player_circles(board)
                #pygame.display.update()
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


################        GUI METHODS     #########################

def display_board(board):
    pygame.init()
    pygame.font.init() 
    size = (width,height)
    global screen
    #screen = menu.screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")

    screen.fill(WHITE)                  # entire screen is white
    screen.fill(BOARDCOLOR,(0,SQUARESIZE,width,height))         #now only rest of screen expect the top bar is BOARDCOLOR
    draw_inital_circles(board)                          # adds circles/holes to the board
    pygame.display.flip()

def check_events(board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            continue            

# Function that adds empty circles to the board
def draw_inital_circles(board):
        
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            position = (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2)
            radius = (SQUARESIZE//2 -5)        
            pygame.draw.circle(screen,WHITE,position ,radius)


# Function that adds player circles to the board         
def draw_player_circles(board):
    draw_inital_circles(board)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            #Here player piece height differs from initial circles since the board is flipped it adds backwards that why we subtract from height
            #Also we have to accomodate for the top bar that takes height of SQUARESIZE 
            position = (c*SQUARESIZE+SQUARESIZE//2, height - int(r*SQUARESIZE+SQUARESIZE/2))
            radius = (SQUARESIZE//2 -5)        
   
            if(board[r][c] == 1):       #PLAYER 1 PIECE
                pygame.draw.circle(screen,RED,position ,radius)
            elif(board[r][c] == 2):     #PLAYER 2 PIECE
                pygame.draw.circle(screen,BLUE,position ,radius)

            #else:                       #EMPTY CIRCLE THEN IGNORE
            #pygame.draw.circle(screen,color,position ,radius)
            #pygame.draw.circle(screen,color,position ,radius)
    pygame.display.update()

def draw_gameover(board,playerNo):
    #font = pygame.font.SysFont("segoeui", 60,True)            # Font used Arial size 50 in BOLD
    font=pygame.font.Font("slkscre.ttf", 60)
    #creates a surface for text to be rendered on it, False for 24-bit image, 
    color = (0,0,0)     #black color
    winner = "Red" if(playerNo == 1) else "Blue"
    txtsurf = font.render(winner+" Wins", False, winner)
    
    screen.blit(txtsurf,  (80 ,30)  )
    pygame.display.update()

def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if is_valid_column(board, col):
			valid_locations.append(col)
	return valid_locations

def get_winner(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True
	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True