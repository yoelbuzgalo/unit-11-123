from mixed_fractions import *

# YOU MAY USE THIS FILE TO DEBUG YOUR CODE.

def main():
    tuples = [(3, 7, 17), (2, 0, 1), (3, -1, 1), (-6, 8, -15),(1, 2, 18),
              (1, 11, 10), (-3, 10, 2), (1, 18, 3), (-6, -8, 15), (-5, 23, -15), 
              (1, 14, 17), (0, 15, 2), (2, 3, 11), (1, -16, -8), (1, 2, 18), 
              (1, 11, 18), (3, 6, 4), (0, 12, 17), (3, 11, 19), (0, 14, 9), 
              (-3, -14, -34), (0, -7, -3), (-6, 9, -15), (3, -7, -17), (3, 11, 14), 
              (3, 70, 170), (1, 1, 1), (0, 13, 18), (1, -49, -19), (2, 14, 20), 
              (1, 9, 10), (3, 11, 14), (1, 34, 14), (2, 20, 14), (1, 12, 17), 
              (0, 5, 17), (1, 2, 18), (3, 6, 4), (1, 11, 8), (2, 0, -1), 
              (3, 11, 14), (-3, -20, 2), (0, 14, 2), (1, 2, 18), (0, 9, 3), 
              (1, 34, 20), (0, 13, 18), (-10, 0, 5), (1, 22, -2), (0, -12, -4), 
              (4, 2, 4), (1, 8, 10), (1, 18, 3), (2, 0, 10), (0, 15, 8), 
              (2, 3, 9), (3, 11, 14), (3, 0, 17)]
    fractions = [Fraction(w, n, d) for w, n, d in tuples]
    # manual_test_unique_sorted_list(fractions)
    # manual_test_partition(fractions)
    # manual_test_find_all(fractions)
    
'''        
def manual_test_unique_sorted_list(fractions):  
    print("Test 1:", unique_sorted_list(fractions[:3]))     # [<2, 0, 1>, <3, 7, 17>]
    print("Test 2:", unique_sorted_list(fractions[:5]))     # [<-6, 8, -15>, <1, 2, 18>, <2, 0, 1>, <3, 7, 17>]
    print("Test 3:", unique_sorted_list(fractions[:10]))    # [<-6, 8, -15>, <1, 2, 18>, <2, 0, 1>, <1, 11, 10>, <3, 7, 17>, <1, 18, 3>]
    sorted = unique_sorted_list(fractions) 
    print("Test 4:", sorted)                                # [<-3, -20, 2>, <-10, 0, 5>, <-6, 9, -15>, <-6, 8, -15>, <-3, -14, -34>, <0, 5, 17>, <0, 12, 17>, <0, 13, 18>, <1, 2, 18>, <0, 14, 9>, <1, 11, 18>, <1, 12, 17>, <1, 8, 10>, <1, 14, 17>, <0, 15, 8>, <1, 9, 10>, <2, 0, 1>, <1, 11, 10>, <2, 3, 11>, <0, -7, -3>, <1, 11, 8>, <2, 14, 20>, <1, -16, -8>, <3, 7, 17>, <1, 34, 14>, <3, 11, 19>, <3, 11, 14>, <3, 6, 4>, <1, 18, 3>, <0, 15, 2>]
    print("Test 5:", len(sorted))                           # 30
'''

'''
def manual_test_partition(fractions): 
    a_partition = partition(fractions)
    print("Test 6:", a_partition[Fraction(3, 70, 170)])     # [<3, 7, 17>, <3, -7, -17>, <3, 70, 170>]
    print("Test 7:", Fraction(5, 6, 7) in a_partition)      # False
'''

'''
def manual_test_find_all(fractions):
    a_partition = partition(fractions)
    print("Test 8:", find_all(a_partition, Fraction(-5, -10, 2)))   # [<-10, 0, 5>, <1, 22, -2>]
    print("Test 9:", find_all(a_partition, Fraction(2)))            # [<2, 0, 1>, <3, -1, 1>, <-3, 10, 2>, <1, 1, 1>, <2, 0, -1>, <2, 0, 10>]
    print("Test 10:", find_all(a_partition, Fraction(-6, -8, 15)))  # [<-6, 8, -15>, <-6, -8, 15>, <-5, 23, -15>]
    print("Test 11:", find_all(a_partition, Fraction(5, 6, 7)))     # []
'''

if __name__ == "__main__":       
    main()  