# Load modules
from logic import *

            
class Player():
    last_move = [None, None]
    moves = []
    
    def __init__(self, board, color):
        self.board = board
    
        self.piece_indexes = {
        0: Pawn,
        1: Horse,
        2: Bishop,
        3: Rook,
        4: Queen,
        5: King
       }
        
        self.castling = [False, False, False, False]
        
         
        if color == 'white':
            self.color = 1
        if color == 'black':
            self.color = 0
    
    def startRound(self):
        Logic.AtkByEnemy(self)
        #Logic.showPossibleMoves(self, self.board)
    
    def pickPiece(self, position):
        self.moves = []    
        self.last_move = [None, None]
        self.last_move[0] = None
        self.last_move[1] = None
        for i in range(8):
            for j in range(8):
                if position[0] in range(self.board.squares[i][j].left_border, self.board.squares[i][j].right_border) and \
                    position[1] in range(self.board.squares[i][j].top_border, self.board.squares[i][j].bot_border):
                    if self.board.squares[i][j].img != None and self.board.squares[i][j].piece_color == self.color:
                        self.last_move[0] = i
                        self.last_move[1] = j
                        Logic.showMoves(self)
                            
                            

    def movePiece(self, position):
        for i in range(8):
            for j in range(8):
                if position[0] in range(self.board.squares[i][j].left_border, self.board.squares[i][j].right_border) and \
                    position[1] in range(self.board.squares[i][j].top_border, self.board.squares[i][j].bot_border):
                    if (i != self.last_move[0] or j != self.last_move[1]) and self.last_move[0] != None and self.last_move[1] != None:
                        for move in self.moves:
                            if i == move[0] and j == move[1]:
                                self.board.squares[i][j].mapPiece(self.board.squares[self.last_move[0]][self.last_move[1]])
                                self.board.squares[i][j].piece_moved = True
                                self.board.squares[self.last_move[0]][self.last_move[1]].clearSquare() 

                                Logic.resetEnPassant(self) # Resetting en_passant from last round
                                
                                # Castling cases
                                if self.board.squares[i][j].piece_index == 5:
                                    Logic.checkIfCastled(self, i, j)

                                # Pawn double move cases (For en passant)
                                if self.board.squares[i][j].piece_index == 0:
                                    Logic.checkIfDoubleMove(self, i, self.last_move[1], j)
                                    Logic.destroyAfterEnPassant(self, i, j)
                                
                                return(1)
                            
                        