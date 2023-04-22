from board import *
from bishop import Bishop
from rook import Rook

class Queen:

    def showMoves(self, x, y):
        possible_moves = []

        for move in Bishop.showMoves(self, x, y):
            possible_moves.append(move)
            
        for move in Rook.showMoves(self, x, y):
            possible_moves.append(move)
       
        return(possible_moves)