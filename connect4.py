import random
import sys
import time
import pygame
import board as bd
import menu 
import minimax as mn


# sequence goes as follows start menu which returns the board and displays the game screen
board,easy_mode,minimax = menu.main_menu()      
game_over = False
turn = random.randint(1,2)  # variable to indicate whose turn it is, first player is randomly choosen
is_first_Time = True
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if turn == 1:
        column = random.randint(0, 6)
        print("COLUMN=",column)
        if(bd.is_valid_column(board, column)):    #checks to see if there is an empty space
            row_column = bd.add_piece(board, column, 1)   # adds piece and stores the place it was added
            bd.draw_player_circles(board)
            if(bd.winning_move(board, 1, row_column[0], row_column[1])):
                bd.draw_gameover(board,1)
                print("Player one won !!!") 
                game_over = True
                pygame.time.wait(2000)

                break
            pygame.time.wait(1500)
            
        turn = 2    # changes turn so it's player 2
    
    # player 2 turn AI
    else:
        
        if easy_mode:
            depth = 2
        else:
            depth = 5
        
        if(is_first_Time == True):
            column = 3
            is_first_Time = False
        else:
            column =  mn.minimax(board,depth,True)[0] if minimax else mn.alpha_beta(board,-1000000,1000000,depth,True)[0]
       
        if(bd.is_valid_column(board, column)):    #checks to see if there is an empty space
            row_column = bd.add_piece(board, column, 2)   # adds piece and stores the place it was added
            bd.draw_player_circles(board)
            if(bd.winning_move(board, 2, row_column[0], row_column[1])):
                bd.draw_gameover(board,2)
                print("Player two won !!!")
                game_over = True
                pygame.time.wait(2000)
                break
            pygame.time.wait(1500)
        turn = 1     #changes turn so it's player 1
#bd.print_board(board)