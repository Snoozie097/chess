# Import libraries
import pygame
import os
from pygame.locals import *
# Load modules
from squares import *


class Board():
    # Set the width and height of the GUI window
    WIDTH = 800
    HEIGHT = 800
    
    # Create a window with specified dimensions
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    
    def __init__(self):
        # Initialize the attributes of the chessboard.
        self.columns = [0, 1, 2, 3, 4, 5, 6, 7]
        self.rows = [0, 1, 2, 3, 4, 5, 6, 7]
        self.rect_width = self.WIDTH/8
        self.rect_height = self.HEIGHT/8
        self.light = (225, 200, 150) # Color of light squares
        self.dark = (160, 135, 100) # Color of dark squares
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) # Res of window
        self.squares = [['_' for i in range(8)] for i in range(8)]

        x = y = 0
        # Drawing chessboard squares and initializing squares objects
        # Loop over the columns and rowns, then draw squares on the chessboard and init squares.
        for COLUMN in self.columns:
            for ROW in self.rows:
                rect = pygame.Rect(y, x, self.rect_height, self.rect_width)
                self.squares[COLUMN][ROW] = Squares(y, y + self.rect_width, x, x + self.rect_height)
                
                if (COLUMN + ROW) % 2 == 0:
                    pygame.draw.rect(self.surface, self.light, rect)
                    x += self.rect_width
                else:
                    pygame.draw.rect(self.surface, self.dark, rect)
                    x += self.rect_width
            x = 0
            y += self.rect_height
            
            
       # Drawing chessboard squares w/o initializing squares objects
    def drawBoard(self):
        # Initialize the position variables.
        x = y = 0

        # Loop over the columns and rowns, then draw squares on the chessboard.
        for COLUMN in self.columns:
            for ROW in self.rows:
                rect = pygame.Rect(y, x, self.rect_height, self.rect_width)
                if (COLUMN + ROW) % 2 == 0:
                    pygame.draw.rect(self.surface, self.light, rect)
                    x += self.rect_width
                else:
                    pygame.draw.rect(self.surface, self.dark, rect)
                    x += self.rect_width
            x = 0
            y += self.rect_height
            
    # Draw pieces on board        
    def loadPieces(self):
        for x in range(8):
            for y in range(8):
                # If the square has an image, draw the image on the chessboard
                if self.squares[x][y].img != None:
                    self.WINDOW.blit(self.squares[x][y].img, (self.squares[x][y].left_border, self.squares[x][y].top_border))


    # Import position from FEN
    def mapFEN(self, FEN):
        # If there is no input of FEN, give default FEN
        if FEN == '':
            FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        else: FEN = FEN

        # Initialize squares indexes variables
        i = 0
        j = 0

        # Dictionary mapping piece info to letters in FEN
        map_pieces = {
            "P": (pygame.image.load(os.path.join('pieces','white_pawn.png')), 0, 1),
            "p": (pygame.image.load(os.path.join('pieces','black_pawn.png')), 0, 0),
            "N": (pygame.image.load(os.path.join('pieces','white_horse.png')), 1, 1),
            "n": (pygame.image.load(os.path.join('pieces','black_horse.png')), 1, 0),
            "B": (pygame.image.load(os.path.join('pieces','white_bishop.png')), 2, 1),
            "b": (pygame.image.load(os.path.join('pieces','black_bishop.png')), 2, 0),
            "R": (pygame.image.load(os.path.join('pieces','white_rook.png')), 3, 1),
            "r": (pygame.image.load(os.path.join('pieces','black_rook.png')), 3, 0),
            "Q": (pygame.image.load(os.path.join('pieces','white_queen.png')), 4, 1),
            "q": (pygame.image.load(os.path.join('pieces','black_queen.png')), 4, 0),
            "K": (pygame.image.load(os.path.join('pieces','white_king.png')), 5, 1),
            "k": (pygame.image.load(os.path.join('pieces','black_king.png')), 5, 0)
        }

        # Loop that goes thru every character in FEN
        for x in FEN:
            if x in map_pieces:
                img, piece_index, piece_color = map_pieces[x]
                self.squares[i][j].img = img
                self.squares[i][j].piece_index = piece_index
                self.squares[i][j].piece_color = piece_color
                self.squares[i][j].occupied = 1
                i += 1
            elif x == '/':
                j += 1
                i = 0
            elif x.isnumeric():
                i += int(x)

    