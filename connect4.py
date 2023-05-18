import sys
import time
import pygame
import board as bd
import menu 
import minimax as mn


board = menu.main_menu()
#board = bd.create_board()  # creates a new board to play
game_over = False
turn = 1  # variable to indicate whose turn it is, right now it's player one
#menu.main_menu()
bd.print_board(board)
#bd.display_board(board)

while not game_over:
        #bd.check_events(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                #player 1 turn
                if turn == 1:
                    column = event.pos[0]             #returns x coordinate for click position
                    column = column // 100              #convert the x coordinate to column num x= 610 means column 6 
                    print(column)
                    if(bd.is_valid_column(board, column)):    #checks to see if there is an empty space
                        row_column = bd.add_piece(board, column, 1)   # adds piece and stores the place it was added
                        if(bd.winning_move(board, 1, row_column[0], row_column[1])):
                            bd.draw_gameover(board,1)
                            print("Player one won !!!")
                            game_over = True
                            pygame.time.wait(1000)
                    turn = 2    # changes turn so it's player 2
                
                # player 2 turn
                else:
                    #column = (event.pos[0]) // 100
                    column , minimax_score = mn.minimax(board,2,True)

                    if(bd.is_valid_column(board, column)):    #checks to see if there is an empty space
                        row_column = bd.add_piece(board, column, 2)   # adds piece and stores the place it was added
                        if(bd.winning_move(board, 2, row_column[0], row_column[1])):
                            bd.draw_gameover(board,2)
                            print("Player two won !!!")
                            game_over = True
                            pygame.time.wait(1000)
                    turn = 1     #changes turn so it's player 1
            bd.print_board(board)