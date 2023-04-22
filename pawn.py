from board import *

class Pawn:

    def showMoves(self, x, y):
        possible_moves = []
        p = []

        if self.color == 0:
            # Moving forward
            try:
                if self.board.squares[x][y+1].occupied == 0: p.append([x, y+1])
            except IndexError:
                pass
            
            # Double move
            if y == 1:
                if self.board.squares[x][y+2].occupied == 0: p.append([x, y+2])

            # Capturing pieces
            try: 
                if self.board.squares[x-1][y+1].piece_color == 1: p.append([x-1, y+1])
                if self.board.squares[x-1][y+1].w_en_passant == True: p.append([x-1, y+1])
            except IndexError: 
                pass
            try: 
                if self.board.squares[x+1][y+1].piece_color == 1: p.append([x+1, y+1])
                if self.board.squares[x+1][y+1].w_en_passant == True: p.append([x+1, y+1])
            except IndexError: 
                pass
                
        if self.color == 1:
            # Moving forward
            try:
                if self.board.squares[x][y-1].occupied == 0: p.append([x, y-1])
            except IndexError:
                pass
            
            # Double move
            if y == 6:
                if self.board.squares[x][y-2].occupied == 0: p.append([x, y-2])
            
            # Capturing pieces
            try: 
                if self.board.squares[x-1][y-1].piece_color == 0: p.append([x-1, y-1])
                if self.board.squares[x-1][y-1].b_en_passant == True: p.append([x-1, y-1])
            except IndexError: 
                pass
            try: 
                if self.board.squares[x+1][y-1].piece_color == 0: p.append([x+1, y-1])
                if self.board.squares[x+1][y-1].b_en_passant == True: p.append([x+1, y-1])
            except IndexError: 
                pass
            
        for move in p:
            possible_moves.append(move)

        return possible_moves