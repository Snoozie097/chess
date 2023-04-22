class Squares():
    img = None
    piece_index = None
    piece_color = None
    occupied = 0
    piece_moved = False
    w_en_passant = False
    b_en_passant = False
    under_atk= False

    def __init__(self, left_border, right_border, top_border, bot_border):
        self.left_border = int(left_border)
        self.right_border = int(right_border)
        self.top_border = int(top_border) 
        self.bot_border = int(bot_border)
        self.x_middle = (left_border + right_border)/2
        self.y_middle = (top_border + bot_border)/2
        
    def mapPiece(self, Squares):
            self.img = Squares.img
            self.piece_index = Squares.piece_index
            self.piece_color = Squares.piece_color
            self.occupied = Squares.occupied
    
    def clearSquare(self):
        self.img = None
        self.piece_index = None
        self.piece_color = None
        self.occupied = 0

