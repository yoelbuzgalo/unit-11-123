
NAME_TO_TABLE = {'t': [[1,1,1],[0,1,0]], 
                 'T': [[1,1,1],[0,1,0],[0,1,0]], 
                 'z': [[1,1,0],[0,1,1]],
                 'c': [[1,1],[1,0],[1,1]],
                 'f': [[1,1],[1,0],[1,1], [1,0]],
                 'L': [[1,0,0],[1,1,1]],
                 'l':[[1,0], [1,1]]}
EMPTY_SPOT = '-'
BLOCKER_SPOT = 'o'

def f(M):
    return [[ M[col][row] for col in range(len(M))] for row in range(len(M[0]))]

def g(M):
    return M[::-1]

def h(M):
    return [M[row][::-1] for row in range(len(M)) ]

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
    
    def get_table(self):
        return self.__table      
          
class Puzzle:
    __slots__ = ['__board', '__pieces', '__pieces_on_board', '__game_over']
    
    def __init__(self, blockers):
        self.__board = [[EMPTY_SPOT for _ in range(6)] for _ in range(6)]
        for r, c in blockers:
            self.__board[r][c] = BLOCKER_SPOT
               
    def play(self):
        print(self)
        while True:
            response = input("Enter a command or 'help': ")
            if response == "quit":
                print("Bye!")
                break
            elif response == "help":
                help_message()
            else:
                pass
    
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