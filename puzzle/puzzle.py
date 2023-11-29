
NAME_TO_TABLE = {'t': [[1,1,1],[0,1,0]], 
                 'T': [[1,1,1],[0,1,0],[0,1,0]], 
                 'z': [[1,1,0],[0,1,1]],
                 'c': [[1,1],[1,0],[1,1]],
                 'f': [[1,1],[1,0],[1,1], [1,0]],
                 'L': [[1,0,0],[1,1,1]],
                 'l':[[1,0], [1,1]]}
EMPTY_SPOT = '-'
BLOCKER_SPOT = 'o'

def transpose(M):
    return [[ M[col][row] for col in range(len(M))] for row in range(len(M[0]))]

def rev_row(M):
    return M[::-1]

def rev_column(M):
    return [M[row][::-1] for row in range(len(M))]

def help_message():
    print("- 'help' to display commands")
    print("- 'quit' to quit the game" )
    print("- 'a <piece name> <row> <col>' to add a piece to the board at the position ") 
    print("- 'r <piece name>' to remove a piece")
    
class Shape:
    __slots__ = ['__table', '__position'] 
    
    def __init__(self, table):
        self.__table = table
        self.__position = None        
    
    def __hash__(self):
        return hash(str(self.__table))
    
    def __repr__(self):
        return str(self.__table)\
            + " " + str(self.__position)\
            
    def __eq__(self, other):
        if type(self) == type(other):
            if self.__table == other.__table:
                return True
        return False
    
    def fit(self,board, position):
        row, col = position # Get the board position
        # Iterate over row and column of shape table
        for i in range(len(self.__table)):
            for j in range(len(self.__table[i])):
                    if (row+i) < len(board) and (col+j) < len(board[row+i]):
                        if (self.__table[i][j] == 1 and board[row+i][col+j] == "-") or (self.__table[i][j] == 0):
                            continue
                        else:
                            return False
                    else:
                        # In case where board[row+i] or board[col+j] is an invalid position (out of array), itll return False and not crash program
                        return False
        return True
    
    def add(self, board, position, symbol):
        self.__position = position
        row, col = self.__position
        for i in range(len(self.__table)):
            for j in range(len(self.__table[i])):
                if self.__table[i][j] == 1:
                    board[row+i][col+j] = symbol
        return
    
    def remove(self, board):
        if self.__position != None:
            row, col = self.__position
            for i in range(len(self.__table)):
                for j in range(len(self.__table[i])):
                    if self.__table[i][j] == 1:
                        board[row+i][col+j] = "-"
        return

    def get_table(self):
        return self.__table

class Piece:
    __slots__ = ['__name','__current_shape', '__fit_shapes', '__choice']
    def __init__(self, name):
          self.__name = name
          self.__current_shape = None
          self.__fit_shapes = []
          self.__choice = 0
    
    def get_name(self):
        return self.__name
    
    def get_current_shape(self):
        return self.__current_shape
    
    def add(self, board, shape, position):
        shape.add(board, position,self.get_name())
        self.__current_shape = shape
    
    def remove(self, board):
        self.__current_shape.remove(board)
        self.__current_shape = None
    
    def get_fit_shapes(self):
        return self.__fit_shapes
    
    def get_fit_shape(self):
        if len(self.__fit_shapes) == 0:
            return None
        choice = self.__fit_shapes[self.__choice]
        self.__choice = (self.__choice + 1) % len(self.__fit_shapes)
        return choice
    
    def create_shape(self,shape,board,position):
        if shape.fit(board, position):
            self.__fit_shapes.append(shape)

    def set_fit_shapes(self, board, position):
        original_shape = Shape(NAME_TO_TABLE[self.__name])
        self.create_shape(original_shape, board, position)

        rev_col_shape = Shape(rev_column(original_shape.get_table())) # Reverse column the original shape
        self.create_shape(rev_col_shape, board, position)

        rev_row_shape = Shape(rev_row(original_shape.get_table())) # Reverse row the original shape
        self.create_shape(rev_row_shape, board, position)

        rev_col_row_shape = Shape(rev_column(rev_row(original_shape.get_table()))) # Reverse row the reversed column shape
        self.create_shape(rev_col_row_shape, board, position)
        
        transposed_shape = Shape(transpose(original_shape.get_table())) # Transpose the shape
        self.create_shape(transposed_shape, board, position)

        rev_row_trans_shape = Shape(rev_row(transposed_shape.get_table())) # Reverse row the transposed shape
        self.create_shape(rev_row_trans_shape, board, position)

        rev_col_trans_shape = Shape(rev_column(transposed_shape.get_table())) # Reverse column the transposed shape
        self.create_shape(rev_col_trans_shape, board, position)

        rev_row_col_trans_shape = Shape(rev_row(rev_column(transposed_shape.get_table()))) #Reverse the row and column of transposed shape
        self.create_shape(rev_row_col_trans_shape, board, position)


class Puzzle:
    __slots__ = ['__board', '__pieces', '__pieces_on_board', '__game_over']
    
    def __init__(self, blockers):
        self.__board = [[EMPTY_SPOT for _ in range(6)] for _ in range(6)]
        for r, c in blockers:
            self.__board[r][c] = BLOCKER_SPOT
        self.__pieces = {}
        self.__pieces_on_board = {}
        for name in NAME_TO_TABLE:
            self.__pieces[name] = Piece(name)
               
    def play(self):
        print(self)
        while True:
            response = input("Enter a command or 'help': ")
            response_splitted = response.split(" ")
            if response == "quit":
                print("Bye!")
                break
            elif response == "help":
                help_message()
            elif response_splitted[0] == "a":
                # Add function goes here
                name = response_splitted[1]
                if not (name in self.__pieces):
                    print("Invalid letter piece")
                    continue
                position = (int(response_splitted[2]), int(response_splitted[3]))
                piece = Piece(name)
                piece.set_fit_shapes(self.__board, position)
                if len(piece.get_fit_shapes()) == 0:
                    print("Please try different position, blocked.")
                else:
                    list_of_shapes = piece.get_fit_shapes()
                    selected = False
                    while selected is False:
                        current = piece.get_fit_shape()
                        piece.add(self.__board, current, position)
                        print(self)
                        user_input = input(name+": "+"Like this?(y/n) ")
                        if user_input == "n":
                            piece.remove(self.__board)
                            continue
                        elif user_input == "y":
                            self.__pieces_on_board[name] = piece
                            self.__pieces.pop(name)
                            selected = True
                            break
                        else:
                            print("Invalid input")
            elif response_splitted[0] == "p":
                print(self)
            elif response_splitted[0] == "r":
                name = response_splitted[1]
                if name in self.__pieces_on_board:
                    piece = self.__pieces_on_board[name]
                    piece.remove(self.__board)
                    self.__pieces_on_board.pop(name)
                    self.__pieces[name] = Piece(name)
                else:
                    print("Piece isn't on the board!")
    
    def __str__(self):
        s = '    0 1 2 3 4 5\n'
        s +='   ------------\n'
        for index in range(len(self.__board)):
            s += str(index) + " | "
            for elt in self.__board[index]:
                s += elt + " "
            s += "\n"
        return s
     
def main(): 
    # blocker_locations = ((0,1), (0,5), (2,0), (5,1), (5,4))
    # blocker_locations = ((0,0), (0,1), (3,4), (4,0), (5,5))
    blocker_locations = ((0,1), (0,3), (4,3), (5,3), (5,5)) 
    a_puzzle = Puzzle(blocker_locations)
    a_puzzle.play()
    
if __name__ == '__main__':     
    main()