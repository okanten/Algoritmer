
class Chess:
    
    def __init__(self, board_size: int = 5):
        self.board_size = board_size
        self.board = self.generate_chess_board()
        self.free_space = 0
 
    def generate_chess_board(self):
        # Generate a board, and set each slot to None (unoccupied)
        board = [[None for n in range(self.board_size)] for nn in range(self.board_size)]
        return board

    def get_size(self):
        return self.board_size

    def get_chess_board(self):
        return self.board

    def get_piece_on_position(self, position_dictionary):
        x, y = positon_dictionary['x'], position_dictionary['y']
        return self.board[x][y]

    def set_piece_on_position(self, position_dictionary, piece):
        x, y = position_dictionary['x'], position_dictionary['y']
        if not self.square_is_free_or_can_be_taken(position_dictionary, piece.color):
            self.board[x][y] = piece
            return True
        return False

    def square_is_free_or_can_be_taken(self, position_dictionary, piece_color: int):
        """
            Checks if square on board is occupied, and if its occupied, then check if the piece is opposite colour
        """
        piece = self.get_piece_on_position(position_dictionary)
        return (piece is None or piece.color != piece_color)


class Piece(Chess):

    def __init__(self, legal_move_x: list(), legal_move_y: list(), identifier: int = 99, board_size: int = 8, color: int = 1):
        """
            Create a new piece with a set amount of legal x, y moves (explained further down).
            An identifier to differentiate a pawn from (for example) a queen. Default value (99) symbolizes blocked
            Board size is pretty self explanatory, but it is n * n.
            Color identifies which color the piece is (black = 0, white = 1)

            legal_move_x and legal_move_y need to share the same index and key value according to the path allowed.
            i.e: a Knight can move in an L shape. The arrays need to be like this in some order: 
                x = [1, 2, -1, -2,  1,  2, -1, -2]
                y = [2, 1, -2, -1, -2, -1,  2,  1] 

            that way x[0], y[0] make up a legal move, like so:
            [1, 2]
        """
        self.legal_moves = list()
        for i in range(len(legal_move_x)):
            tmp_list = [legal_move_x[i], legal_move_y[i]]
            self.legal_moves.append(tmp_list)
        self.identifier = identifier
        # Store position in a dictionary. Key-value pair
        self.position = {'x': 0, 'y': 0}
        self.color = color
        super().__init__(board_size)
        print(self.board)

    def is_legal_move(self, x, y):
        """ Create a temporary array with parameters and check if its in legal moves. Returns True/False """
        tmp_list = [x, y]
        return tmp_list in self.legal_moves 

    def move_piece_by(self, x: int = 0, y: int = 0):
        """
            Move the piece by adding (or subtracting) based on axis
            i.e: position is already [3, 2]. Move it by one up and two steps to the left doing this:
            move_piece_by(-1, -2)
            position will then be updated to: [2, 0], and it will be here on a 5 x 5 board where the upper left corner is [0, 0] and the center is [2, 2]:

            [x, x, x, x, x,
             x, x, x, x, x,
             P, x, x, x, x,
             x, x, x, x, x,
             x, x, x, x, x]
        """
        if self.is_legal_move(x, y):
            return self.set_piece_on_position({'x': x, 'y': y})
        return False

    def set_position(self, x: int = None, y: int = None):
        """
            Updates the position for the piece. The parameters have type hints to make it clear that its purely integers and not a combination (e.g 8A)
            We also have default values (set to None, that we later check) to make it possible to only update one of the values (useful for Queens and Pawns)
        """
        if x is None:
            x = self.position['x']
        if y is None:
            y = self.position['y']
        self.position['x'] = x
        self.position['y'] = y

    def set_position_with_dict(self, position_dict: dict):
        """
            Updates the position for the piece by dictionary (override)        
        """
        self.position = position_dict
        

    def get_position(self) -> dict:
        return self.position

class Knight(Piece):

    def __init__(self, position: dict = None, board_size: int = 8, color: int = 1):
        # Vi bruker disse sammen
        legal_move_x = [1, 2, -1, -2,  1,  2, -1, -2]
        legal_move_y = [2, 1, -2, -1, -2, -1,  2,  1] 
        identifier = 5
        super().__init__(legal_move_x, legal_move_y, identifier, board_size, color)
        print(self.legal_moves)
        if position is None:
            position = {'x': 0, 'y': 0}
        super().set_position_with_dict(position)
    
    

s = Knight(board_size=5)

print(s.is_legal_move(2, 1))
s.is_legal_move(1, 2)
s.is_legal_move(1, 1)
s.is_legal_move(-2, 1)
