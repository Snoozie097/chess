# Import libraries
import pygame
import sys
from board import *
from player import *

# Open window
pygame.init()

# Init board object
board = Board()
# Init players
player1 = Player(board, 'white')
player2 = Player(board, 'black')
# Init logic
#logic = Logic(board)


# Read FEN, draw board and draw pieces
board.mapFEN('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
board.drawBoard()
board.loadPieces()

#   Main Game loop
def mainloop():

    move = 0
    player2.startRound()

    while True:        
        if (move + 2) % 2 == 0: round = player1; last_round = player2
        if (move + 2) % 2 == 1: round = player2; last_round = player1

        pygame.display.update()        
        Logic.showPossibleMoves(round, board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == MOUSEBUTTONDOWN:
                round.pickPiece(pygame.mouse.get_pos())
               

            if event.type == MOUSEBUTTONUP:
                try:
                    move += round.movePiece(pygame.mouse.get_pos())
                    board.drawBoard()
                    board.loadPieces()
                    round.startRound()      
                except TypeError:
                    board.drawBoard()
                    board.loadPieces()
                    pass

mainloop()
