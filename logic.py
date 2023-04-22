# Load modules
from board import *
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King


class Logic:
        
    def showMoves(self):
        self.castling = [False, False, False, False]
        if self.last_move[0] is not None and self.last_move[1] is not None:
            if self.board.squares[self.last_move[0]][self.last_move[1]].piece_index in self.piece_indexes:
                moves = self.piece_indexes[self.board.squares[self.last_move[0]][self.last_move[1]].piece_index].\
                    showMoves(self, self.last_move[0], self.last_move[1])
                for move in moves:
                    self.moves.append(move)

            # King castling moves
            if self.board.squares[self.last_move[0]][self.last_move[1]].piece_index == 5:
                King.checkCastling(self)
                
        for move in self.moves:
            pygame.draw.circle(self.board.surface, (17, 69, 150), \
                (self.board.squares[move[0]][move[1]].x_middle, self.board.squares[move[0]][move[1]].y_middle), 10)
   
   
    def AtkByEnemy(self):
        for i in range(8):
            for j in range(8):
                self.board.squares[i][j].under_atk = False
        for i in range(8):
            for j in range(8):
                if self.board.squares[i][j].piece_color == self.color:
                        moves = self.piece_indexes[self.board.squares[i][j].piece_index].\
                        showMoves(self, i, j)
                        for move in moves:
                            self.board.squares[move[0]][move[1]].under_atk = True

    def checkIfCastled(self, i, j):
        if self.castling[0] == True and i == 6 and j == 0:
            self.board.squares[5][0].mapPiece(self.board.squares[7][0])
            self.board.squares[7][0].clearSquare()    
        if self.castling[1] == True and i == 2 and j == 0:
            self.board.squares[3][0].mapPiece(self.board.squares[0][0])
            self.board.squares[0][0].clearSquare()    
        if self.castling[2] == True and i == 6 and j == 7:
            self.board.squares[5][7].mapPiece(self.board.squares[7][7])
            self.board.squares[7][7].clearSquare()    
        if self.castling[3] == True and i == 2 and j == 7:
            self.board.squares[3][7].mapPiece(self.board.squares[0][7])
            self.board.squares[0][7].clearSquare()  

    def checkIfDoubleMove(self, i, start_j, end_j):
        if abs(start_j - end_j) == 2:
            if self.color == 0: self.board.squares[i][start_j + 1].b_en_passant = True
            if self.color == 1: self.board.squares[i][start_j - 1].w_en_passant = True
                
    def resetEnPassant(self):
        for i in range(8):
            for j in range(8):
                if self.color == 0: 
                    self.board.squares[i][j].b_en_passant = False
                if self.color == 1:
                    self.board.squares[i][j].w_en_passant = False
    
    def destroyAfterEnPassant(self, i, j):
        if self.board.squares[i][j].b_en_passant == True:
            self.board.squares[i][j+1].clearSquare()
        if self.board.squares[i][j].w_en_passant == True:
            self.board.squares[i][j-1].clearSquare()
            
    def showPossibleMoves(self, board):
        help_board = board
        self.moves = []
        
        for i in range(8):
            for j in range(8):
                self.castling = [False, False, False, False]
                if help_board.squares[i][j].piece_index in self.piece_indexes\
                    and help_board.squares[i][j].piece_color == self.color:
                    moves = self.piece_indexes[help_board.squares[i][j].piece_index].\
                    showMoves(self, i, j)

                    for move in moves:
                        self.moves.append(move)

                    # King castling moves
                    if help_board.squares[i][j].piece_index == 5:
                        King.checkCastling(self)
                        
                for move in self.moves:
                    pygame.draw.circle(help_board.surface, (255, 0, 0), \
                        (help_board.squares[move[0]][move[1]].x_middle, self.board.squares[move[0]][move[1]].y_middle), 10)