from board import *

class Rook:

    def showMoves(self, x, y):
        possible_moves = []
        p = []

        xh = x
        yh = y
        while xh < 7:
            xh += 1
            if self.board.squares[xh][yh].piece_color == self.color:
                break
            p.append([xh, yh])
            if self.board.squares[xh][yh].occupied == 1:
                break
        xh = x
        yh = y
        while xh > 0:
            xh -= 1
            if self.board.squares[xh][yh].piece_color == self.color:
                break    
            p.append([xh, yh])
            if self.board.squares[xh][yh].occupied == 1:
                break
        
        xh = x
        yh = y
        while yh < 7:
            yh += 1
            if self.board.squares[xh][yh].piece_color == self.color:
                break
            p.append([xh, yh])
            if self.board.squares[xh][yh].occupied == 1:
                break        
        
        xh = x
        yh = y
        while yh > 0:
            yh -= 1
            if self.board.squares[xh][yh].piece_color == self.color:
                break
            p.append([xh, yh])
            if self.board.squares[xh][yh].occupied == 1:
                break
        
        for move in p:
            possible_moves.append(move)

        return possible_moves
