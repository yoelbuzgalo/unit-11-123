import puzzle

TABLE1 = [[1,1], [1,0], [1,1]] 
TABLE2 = [[1,1], [1,0], [1,1]]
TABLE3 = [[1,1,1], [1,0,1]]

BOARD1 = [['o','o','-','-','-','-'],
         ['t','t','t','-','-','-'],
         ['-','t','-','-','-','-'],
         ['-','L','L','z','o','-'],
         ['o','L','z','z','-','-'],
         ['-','L','z','-','-','o']]

BOARD2 = [['o','o','-','-','-','-'],
          ['-','-','-','-','z','-'],
          ['-','-','-','z','z','-'],
          ['-','-','-','z','o','-'],
          ['o','-','-','-','-','-'],
          ['-','-','-','-','-','o']]

def test_shape_repr():
    shape1 = puzzle.Shape(TABLE1)
    assert "[[1, 1], [1, 0], [1, 1]] None" == repr(shape1)

def test_shape_equal1():
    shape1 = puzzle.Shape(TABLE1)
    shape2 = puzzle.Shape(TABLE2)
    assert shape1 == shape2

def test_shape_equal2():
    shape1 = puzzle.Shape(TABLE1)
    shape3 = puzzle.Shape(TABLE3)
    assert not (shape1 == shape3)
   
def test_shape_hash():
    shape1 = puzzle.Shape(TABLE1)
    shape2 = puzzle.Shape(TABLE2)
    shape3 = puzzle.Shape(TABLE3)
    try:
        a_list = [shape1, shape2, shape3] 
        a_set = set(a_list)
        assert 2 == len(a_set)   
    except TypeError:
        assert False, "Unhashable type!"
    
def test_shape_fit1():
    shape = puzzle.Shape([[0,1], [1,1]])
    fitted = shape.fit(BOARD1, (1,2))
    assert fitted == True
    
def test_shape_fit2():
    shape = puzzle.Shape([[0,1], [1,1]])
    fitted = shape.fit(BOARD1, (2,4))
    assert fitted == False

def test_shape_add():
    shape = puzzle.Shape([[0,1], [1,1]])
    shape.add(BOARD1, (1,2), 'l')
    assert 't' == BOARD1[1][2]
    assert 'l' == BOARD1[1][3]
    assert 'l' == BOARD1[2][2]
    assert 'l' == BOARD1[2][3]

def test_shape_remove():
    shape = puzzle.Shape([[0,1], [1,1]])
    shape.add(BOARD1, (1,2), 'l')
    shape.remove(BOARD1)
    assert 't' == BOARD1[1][2]
    assert '-' == BOARD1[1][3]
    assert '-' == BOARD1[2][2]
    assert '-' == BOARD1[2][3]
    
def test_piece_get_fit_shapes():
    piece = puzzle.Piece('L')
    piece.set_fit_shapes(BOARD2, (3,0))
    shapes = piece.get_fit_shapes()
    assert 3 == len(shapes)
    
def test_peice_get_fit_shape():
    piece = puzzle.Piece('L')
    piece.set_fit_shapes(BOARD2, (3,0))
    shapes = piece.get_fit_shapes()
    
    shape1 = piece.get_fit_shape()
    assert shape1 in shapes
    
    shape2 = piece.get_fit_shape()
    assert shape2 in shapes
    assert not (shape2 == shape1)
    
    shape3 = piece.get_fit_shape()
    assert shape3 in shapes
    assert not (shape3 == shape1)
    assert not (shape3 == shape2)    
 
def test_piece_add1():
    piece = puzzle.Piece('L')
    shape = puzzle.Shape([[0, 1], [0, 1], [1, 1]])
    
    piece.add(BOARD2, shape, (3,0))
    
    assert '-' == BOARD2[3][0]
    assert 'L' == BOARD2[3][1]
    assert 'o' == BOARD2[4][0]
    assert 'L' == BOARD2[4][1]
    assert 'L' == BOARD2[5][0]
    assert 'L' == BOARD2[5][1]

def test_piece_add2():
    piece = puzzle.Piece('L')
    shape = puzzle.Shape([[0, 1], [0, 1], [1, 1]])
    
    piece.add(BOARD2, shape, (3,0))   
    
    assert shape == piece.get_current_shape()

def test_piece_remove():
    piece = puzzle.Piece('L')
    shape = puzzle.Shape([[0, 1], [0, 1], [1, 1]])
    piece.add(BOARD2, shape, (3,0)) 
    piece.remove(BOARD2)
    
    assert None == piece.get_current_shape()
    
    assert '-' == BOARD2[3][0]
    assert '-' == BOARD2[3][1]
    assert 'o' == BOARD2[4][0]
    assert '-' == BOARD2[4][1]
    assert '-' == BOARD2[5][0]
    assert '-' == BOARD2[5][1]
