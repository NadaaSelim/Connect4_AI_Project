import sys
import pygame
import board as bd
import button as btn
screen = None
def main_menu():
    pygame.init()
    pygame.display.set_caption("Menu")
    global screen
    screen = pygame.display.set_mode((bd.width,bd.height))
    screen.fill((190,180,180))
    flag = False
    xposCenter = bd.width//2
    font = pygame.font.Font("slkscre.ttf", 50)
    easy_mode = True
    minimax = True
    #font = pygame.font.SysFont("segoeui", 60,True)            # Font used Arial size 50 in BOLD
    Itemsfont = pygame.font.Font("slkscre.ttf", 40)

    EASY_BUTTON = btn.Button( pos=(xposCenter, 150), text_input="Easy", font=Itemsfont,clicked=True)
    HARD_BUTTON = btn.Button( pos=(xposCenter, 250), text_input="Difficult", font=Itemsfont,clicked= False)
    MINIMAX_BUTTON = btn.Button( pos=(xposCenter, 450), text_input="Mini-max", font=Itemsfont,clicked= True)
    AB_BUTTON = btn.Button( pos=(xposCenter, 550), text_input="Alpha-Beta Pruning", font=Itemsfont,clicked=False)
    board = bd.create_board()
    
    while not flag:
        game_pos = pygame.mouse.get_pos()
        DiffText = font.render("Select Difficulty ", False, (0,0,0))
        Diff_rect = DiffText.get_rect(center=(xposCenter, 50))

        AlgText = font.render("Select Algorithm ", False, (0,0,0))
        Alg_rect = DiffText.get_rect(center=(xposCenter, 350))
        img = pygame.image.load("start_btn.png").convert()
        START_BUTTON = btn.Button(pos=(xposCenter, 650), text_input="START", font=font,clicked= False)
        width = img.get_width()
        height = img.get_height()
        img = pygame.transform.scale(img, (int(width * 0.7), int(height * 0.7)))
        
        START_BUTTON = btn.Button.withImage(START_BUTTON,pos=(xposCenter, 650), image=img)
        
        screen.blit(DiffText, Diff_rect)
        screen.blit(AlgText, Alg_rect)
        #screen.blit(img,(xposCenter,600))


        for button in [EASY_BUTTON, HARD_BUTTON,MINIMAX_BUTTON,AB_BUTTON,START_BUTTON]:
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if easy mode is selected then hard mode is unselected and vice versa
                if EASY_BUTTON.checkForInput(game_pos):
                    HARD_BUTTON.setClicked(False)
                    HARD_BUTTON.update(screen)
                    EASY_BUTTON.setClicked(True)
                    EASY_BUTTON.update(screen)
                    easy_mode = True

                if HARD_BUTTON.checkForInput(game_pos):
                    EASY_BUTTON.setClicked(False)
                    EASY_BUTTON.update(screen)
                    easy_mode = False
                    HARD_BUTTON.setClicked(True)
                    HARD_BUTTON.update(screen)
                
                # if MINIMAX alg is selected then AB Pruning alg is unselected and vice versa
                if MINIMAX_BUTTON.checkForInput(game_pos):
                    AB_BUTTON.setClicked(False)
                    AB_BUTTON.update(screen)
                    minimax = True
                    MINIMAX_BUTTON.setClicked(True)
                    MINIMAX_BUTTON.update(screen)
                
                if AB_BUTTON.checkForInput(game_pos):
                    MINIMAX_BUTTON.setClicked(False)
                    MINIMAX_BUTTON.update(screen)
                    minimax = False
                    AB_BUTTON.setClicked(True)
                    AB_BUTTON.update(screen)
                # if MINIMAX_BUTTON.checkForInput(game_pos):
                #     pass

                if START_BUTTON.checkForInput(game_pos):
                    screen.fill((0,0,0))
                    flag = True
                    #pygame.quit()
                    bd.display_board(board)
                    return board,easy_mode,minimax
                    

        pygame.display.update()
        