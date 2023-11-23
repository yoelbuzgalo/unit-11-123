import mixed_fractions

TUPLES = [(3, 1, 2), (3, -1, 1), (2, 0, 1)]
FRACTIONS = [mixed_fractions.Fraction(w, n, d) for w, n, d in TUPLES]

def test_fraction_implementation():
    # Setup
    w = 10
    n = 2
    d = 5

    # Invoke
    fraction_val = mixed_fractions.Fraction(w, n,d)
    result_w, result_n, result_d = fraction_val.get_fraction()

    # Analysis
    assert result_w == w
    assert result_n == n
    assert result_d == d

def test_fraction_simplify_543():
    # Setup
    w = 5
    n = 4
    d = 3

    # Invoke
    result_w, result_n, result_d = mixed_fractions.Fraction(w,n,d).simplify().get_fraction()

    # Analysis
    print(result_w, result_n, result_d)
    assert result_w == 6
    assert result_n == 1
    assert result_d == 3

def test_fraction_simplify_0153():
    # Setup
    w = 0
    n = 15
    d = -3

    # Invoke
    result_w, result_n, result_d = mixed_fractions.Fraction(w,n,d).simplify().get_fraction()

    # Analysis
    print(result_w, result_n, result_d)
    assert result_w == -5
    assert result_n == 0
    assert result_d == 1

def test_fraction_simplify_764():
    # Setup
    w = -7
    n = -6
    d = -4

    # Invoke
    result_w, result_n, result_d = mixed_fractions.Fraction(w,n,d).simplify().get_fraction()

    # Analysis
    print(result_w, result_n, result_d)
    assert result_w == -6
    assert result_n == 1
    assert result_d == 2

def test_sum_fraction_1():
    # Setup
    fraction_1 = mixed_fractions.Fraction(1,1,2)
    fraction_2 = mixed_fractions.Fraction(2,1,4)
    expected = (3,3,4)

    # Invoke
    result = fraction_1.operator(fraction_2, "add")

    # Analysis
    assert result.simplify().get_fraction() == expected

def test_sum_fraction_2():
    # Setup
    fraction_1 = mixed_fractions.Fraction(3,1,2)
    fraction_2 = mixed_fractions.Fraction(2,3,4)
    expected = (6,1,4)

    # Invoke
    result = fraction_1.operator(fraction_2, "add")

    # Analysis
    assert result.simplify().get_fraction() == expected

def test_subtract_fraction_1():
    # Setup
    fraction_1 = mixed_fractions.Fraction(3,1,2)
    fraction_2 = mixed_fractions.Fraction(2,1,4)
    expected = (1,1,4)

    # Invoke
    result = fraction_1.operator(fraction_2, "subtract")

    # Analysis
    assert result.simplify().get_fraction() == expected

def test_subtract_fraction_2():
    # Setup
    fraction_1 = mixed_fractions.Fraction(2,1,2)
    fraction_2 = mixed_fractions.Fraction(3,1,4)
    expected = (-1,1,4)

    # Invoke
    result = fraction_1.operator(fraction_2, "subtract")

    # Analysis
    assert result.simplify().get_fraction() == expected

def test_fraction_equality():
    # Setup
    fraction_1 = mixed_fractions.Fraction(1,2,3)
    fraction_2 = mixed_fractions.Fraction(0, 10, 6)
    expected = True
    
    # Invoke
    result = fraction_1 == fraction_2
    
    # Analysis
    assert result == expected

def test_fraction_sorting():
    # Setup
    fractions = [mixed_fractions.Fraction(-1, 4, 1), mixed_fractions.Fraction(1,2,3), mixed_fractions.Fraction(2)]
    expected = [mixed_fractions.Fraction(1,2,3), mixed_fractions.Fraction(2,0,1), mixed_fractions.Fraction(-1, 4, 1)]
    
    # Invoke
    result = sorted(fractions)

    # Analysis
    assert result == expected

def test_fraction_less_than_equal():
    # Setup
    fraction_1 = mixed_fractions.Fraction(2,4,2)
    fraction_2 = mixed_fractions.Fraction(3,2,3)
    expected = True

    # Invoke
    result = fraction_2 <= fraction_1

    # Analysis
    assert result == expected

def test_fraction_not_equal():
    # Setup
    fraction_1 = mixed_fractions.Fraction(2,4,2)
    fraction_2 = mixed_fractions.Fraction(3,2,3)
    expected = True

    # Invoke
    result = fraction_2 != fraction_1

    # Analysis
    assert result == expected

def test_subtract():
    a_fraction = mixed_fractions.Fraction(0,4,3)  
    b_fraction = mixed_fractions.Fraction(1)
    actual_subtract = a_fraction.operator(b_fraction, "subtract")
    expected_subtract = mixed_fractions.Fraction(0,1,3)
    assert expected_subtract == actual_subtract

def test_sum():
    a_fraction = mixed_fractions.Fraction(1,3,10) # 1.3
    b_fraction = mixed_fractions.Fraction(4,6,10) # 4.6
    expected_sum = mixed_fractions.Fraction(5, 9,10) # 5.9
    actual_sum = a_fraction.operator(b_fraction, "add") 
    assert expected_sum == actual_sum

def test_eq_1():
    a_fraction = mixed_fractions.Fraction(-2, 27,13)  
    b_fraction = mixed_fractions.Fraction(0,7,91)
    assert a_fraction == b_fraction

def test_eq_2():
    x = 199933
    y = 11111111111111111
    z = x*y                 
    a_fraction = mixed_fractions.Fraction(0, z, x)
    b_fraction = mixed_fractions.Fraction(y)
    assert a_fraction == b_fraction

def test_neq():
    a_fraction = mixed_fractions.Fraction(0,100000000000000000,3)
    b_fraction = mixed_fractions.Fraction(0,100000000000000001,3)
    assert a_fraction != b_fraction

def test_lt():
    a_fraction = mixed_fractions.Fraction(0, 100000000000000000,3)
    b_fraction = mixed_fractions.Fraction(0, 100000000000000001,3)
    assert a_fraction < b_fraction 

def test_gt():
    a_fraction = mixed_fractions.Fraction(0,100000000000000000,3)
    b_fraction = mixed_fractions.Fraction(0,100000000000000001,3)
    assert b_fraction > a_fraction

def test_hash_same_num():
    a_fraction = mixed_fractions.Fraction(0, 100, 2) # Should also simplify to 50/1
    b_fraction = mixed_fractions.Fraction(0, 50, 1)

    assert hash(a_fraction) == hash(b_fraction)

def test_hash_different_num():
    a_fraction = mixed_fractions.Fraction(0, 2, 100)
    b_fraction = mixed_fractions.Fraction(0, 100, 2)

    assert hash(a_fraction) != hash(b_fraction)

def test_unique_sorted_list():
    actual = mixed_fractions.unique_sorted_list(FRACTIONS)  
    assert [FRACTIONS[1], FRACTIONS[0]] == actual
    
# def test_partition():
#     actual = mixed_fractions.partition(FRACTIONS)
#     assert 2 == len(actual)
#     assert FRACTIONS[0] in actual
#     assert FRACTIONS[1] in actual
#     assert FRACTIONS[2] in actual
#     assert [FRACTIONS[0]] == actual[FRACTIONS[0]]
#     assert [FRACTIONS[1], FRACTIONS[2]] == actual[FRACTIONS[1]]

# def test_find_all():
#     a_partition = mixed_fractions.partition(FRACTIONS) 
     
#     actual = mixed_fractions.find_all(a_partition, FRACTIONS[0])                                 
#     assert [FRACTIONS[0]] == actual
    
#     actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(2,3,2))  
#     assert [FRACTIONS[0]] == actual
    
#     actual = mixed_fractions.find_all(a_partition, FRACTIONS[2])                                 
#     assert [FRACTIONS[1], FRACTIONS[2]] == actual
    
#     actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(3,-2,2))                                 
#     assert [FRACTIONS[1], FRACTIONS[2]] == actual

# def test_find_all_Empty():
#     a_partition = mixed_fractions.partition(FRACTIONS)
#     actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(1,2,3))                                 
#     assert [] == actual
