# Load modules
from board import *

class Horse:

    def showMoves(self, x, y):
        max_range = range(8)
        possible_moves = []
        p = [
        [x + 2, y + 1],
        [x + 1, y + 2],
        [x - 1, y + 2],
        [x - 2, y + 1],
        [x - 2, y - 1],
        [x - 1, y - 2],
        [x + 1, y - 2],
        [x + 2, y - 1],
        ]

        for move in p:
            if move[0] in max_range:
                if move[1] in max_range: 
                    if self.board.squares[move[0]][move[1]].piece_color != self.color:
                        possible_moves.append(move)
    
        return possible_moves
                