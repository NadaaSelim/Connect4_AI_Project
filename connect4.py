import board as bd


board = bd.create_board()  # creates a new board to play
game_over = False
turn = 1  # variable to indicate whose turn it is, right now it's player one

while not game_over:
    
    # player 1 turn
    if turn == 1:
        column = int(input("select from 0-6: "))
        if(bd.is_valid_column(board, column)):    #checks to see if there is an empty space
            row_column = bd.add_piece(board, column, 1)   # adds piece and stores the place it was added
            if(bd.winning_move(board, 1, row_column[0], row_column[1])):
                print("Player one won !!!")
                game_over = True
        turn = 2    # changes turn so it's player 2
    
    # player 2 turn
    else:
        column = int(input("select from 0-6: "))
        if(bd.is_valid_column(board, column)):    #checks to see if there is an empty space
            row_column = bd.add_piece(board, column, 2)   # adds piece and stores the place it was added
            if(bd.winning_move(board, 2, row_column[0], row_column[1])):
                print("Player two won !!!")
                game_over = True
        turn = 1     #changes turn so it's player 1
    bd.print_board(board)