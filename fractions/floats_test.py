def test_subtract():
    a_fraction = 4/3  
    b_fraction = 1
    actual_subtract = a_fraction - b_fraction
    expected_subtract = 1/3
    assert expected_subtract == actual_subtract

def test_sum():
    a_fraction = 1 + 3/10   # 1.3
    b_fraction = 4 + 6/10   # 4.6
    expected_sum = 5 + 9/10 # 5.9
    actual_sum = a_fraction + b_fraction 
    assert expected_sum == actual_sum

def test_eq_1():
    a_fraction = -2 + 27/13  
    b_fraction = 7/91
    assert a_fraction == b_fraction 
         
def test_eq_2():
    x = 199933
    y = 11111111111111111
    z = x*y                 
    a_fraction = z/x
    b_fraction = y
    assert a_fraction == b_fraction
    
def test_neq():
    a_fraction = 100000000000000000/3
    b_fraction = 100000000000000001/3
    assert a_fraction != b_fraction
    
def test_lt():
    a_fraction = 100000000000000000/3
    b_fraction = 100000000000000001/3
    assert a_fraction < b_fraction 

def test_gt():
    a_fraction = 100000000000000000/3
    b_fraction = 100000000000000001/3
    assert b_fraction > a_fraction