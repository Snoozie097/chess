from board import *
from logic import *

class King:

    def showMoves(self, x, y):
        possible_moves = []
        p = []

        p.append([x + 1, y + 1])
        p.append([x + 1, y])
        p.append([x + 1, y -1])
        p.append([x - 1, y + 1])
        p.append([x - 1, y])
        p.append([x - 1, y - 1])
        p.append([x, y + 1])
        p.append([x, y - 1])

        
        for move in p:
            if move[0] in range(8):
                if move[1] in range(8):
                    if self.board.squares[move[0]][move[1]].piece_color != self.color:
                        possible_moves.append(move)
        return possible_moves

    
    def checkCastling(self):
    
        if self.color == 0:
            if self.board.squares[4][0].piece_index == 5 and self.board.squares[4][0].piece_moved == False and self.board.squares[4][0].under_atk == False:
                if self.board.squares[5][0].occupied == 0 and self.board.squares[5][0].under_atk == False:
                    if self.board.squares[6][0].occupied == 0 and self.board.squares[6][0].under_atk == False:
                        if self.board.squares[7][0].piece_index == 3 and self.board.squares[7][0].piece_moved == False:
                            self.moves.append([6, 0])
                            self.castling[0] = True
                            
                if self.board.squares[3][0].occupied == 0 and self.board.squares[3][0].under_atk == False:
                    if self.board.squares[2][0].occupied == 0 and self.board.squares[2][0].under_atk == False:
                        if self.board.squares[1][0].occupied == 0 and self.board.squares[1][0].under_atk == False:
                            if self.board.squares[0][0].piece_index == 3 and self.board.squares[0][0].piece_moved == False:
                                self.moves.append([2, 0])
                                self.castling[1] = True
                                
        if self.color == 1:
            if self.board.squares[4][7].piece_index == 5 and self.board.squares[4][7].piece_moved == False and self.board.squares[4][7].under_atk == False:
                if self.board.squares[5][7].occupied == 0 and self.board.squares[5][7].under_atk == False:
                    if self.board.squares[6][7].occupied == 0 and self.board.squares[6][7].under_atk == False:
                        if self.board.squares[7][7].piece_index == 3 and self.board.squares[7][7].piece_moved == False:
                            self.moves.append([6, 7])
                            self.castling[2] = True
                            
                if self.board.squares[3][7].occupied == 0 and self.board.squares[3][7].under_atk == False:
                    if self.board.squares[2][7].occupied == 0 and self.board.squares[2][7].under_atk == False:
                        if self.board.squares[1][7].occupied == 0 and self.board.squares[1][7].under_atk == False:
                            if self.board.squares[0][7].piece_index == 3 and self.board.squares[0][7].piece_moved == False:
                                self.moves.append([2, 7])
                            self.castling[3] = True
        