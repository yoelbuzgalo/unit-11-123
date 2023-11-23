class Fraction:
    __slots__ = ['__w','__n', '__d']
    def __init__(self, whole=0, numerator=0, denominator=1):
        self.__w = whole
        self.__n = numerator
        self.__d = denominator

    def __repr__(self):
        return "Whole number:" + str(self.__w)\
                +"\n Numerator:" + str(self.__n)\
                + "\n Denominator:" + str(self.__d)\

    def __str__(self):
        return "<" + str(self.__w) + ", " + str(self.__n) + ", " + str(self.__d) + ">"
    
    def __eq__(self, other):
        if type(self) == type(other):
            w_1, n_1, d_1 = self.simplify().get_fraction()
            w_2, n_2, d_2 = other.simplify().get_fraction()

            if w_1 == w_2 and n_1 == n_2 and d_1 == d_2:
                return True
        return False
    
    def __ne__(self, other):
        if type(self) == type(other):
            w_1, n_1, d_1 = self.simplify().get_fraction()
            w_2, n_2, d_2 = other.simplify().get_fraction()
            if not (w_1 == w_2 and n_1 == n_2 and d_1 == d_2):
                return True
        return False
            
    def __lt__(self, other):
        if type(self) == type(other):
            w_1, n_1, d_1 = self.improper_fraction()
            w_2, n_2, d_2 = other.improper_fraction()

            x = n_1*d_2
            y = n_2*d_1

            if x < y:
                return True
        return False
    
    def __le__(self, other):
        if type(self) == type(other):
            w_1, n_1, d_1 = self.improper_fraction()
            w_2, n_2, d_2 = other.improper_fraction()

            x = n_1*d_2
            y = n_2*d_1

            if x <= y:
                return True
        return False
    
    def __hash__(self):
        w,n,d = self.simplify().get_fraction()
        c = str(w)+"/"+str(n)+"/"+str(d)
        return hash(c)

    def get_fraction(self):
        return (self.__w, self.__n, self.__d)
    
    def improper_fraction(self):
        """
        Helper function that calculates and returns an improper fraction
        """
        return (0, self.__n + (self.__w*self.__d), self.__d)
    
    def simplify(self):
        # Mixed fraction to an improper fraction
        imp_w, imp_n, imp_d = self.improper_fraction()
        
        # Divide both numerator and denominator by gcd
        gcd_val = gcd(imp_n, imp_d)
        n = imp_n//gcd_val
        d = imp_d//gcd_val

        # If the denominator is negative, multiply both numerator and denominator by -1
        if d < 0:
            d = d * -1
            n = n * -1

        w = imp_n//imp_d
        n = n % d
        
        return Fraction(w, n, d)
    
    def operator(self, fraction, type="add"):
        w_1,n_1 ,d_1 = fraction.get_fraction()
        w_2,n_2,d_2 = self.get_fraction()

        
        sum_n = 0
        sum_d = 0

        # Find the common denominator using gcd
        common_d = d_1*d_2 // gcd(d_1, d_2)

        # Multiply and update numerators using the difference between common denominator
        n_1 *= common_d//d_1
        n_2 *= common_d//d_2

        if type == "add":
            sum_w = w_1 + w_2 # Sum of whole numbers
            # Add the numerators up
            sum_n = n_1 + n_2
        elif type == "subtract":
            # Subtract the whole numbers
            sum_w = (w_1 - w_2) * -1
            # Subtract the numerators
            if n_1 > n_2:
                sum_n = n_1 - n_2
            else:
                sum_n = n_2 - n_1
                
        # Set denominator as common denominator
        sum_d = common_d

        return Fraction(sum_w, sum_n, sum_d)

def gcd(a, b):  # greatest common divisor
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def unique_sorted_list(a_list):
    '''
    Returns unique sorted list of fraction
    '''
    unique_fractions = set(a_list)
    sorted_list = list(unique_fractions)
    sorted_list.sort()

    return sorted_list

def partition(a_list):
    """
    This function partitions fractions that are equivilent into their list
    """
    hashed_fraction_dict = dict()

    for fraction in a_list:
        if hash(fraction) not in hashed_fraction_dict:
            hashed_fraction_dict[hash(fraction)] = [fraction]
        else:
            hashed_fraction_dict[hash(fraction)].append(fraction)

    fraction_dict = dict()

    for fraction in a_list:
        fraction_dict[fraction] = hashed_fraction_dict[hash(fraction)]
    
    return fraction_dict

def find_all(partition, fraction):
    """
    Returns a list of fraction that is equivilent to the fraction
    """
    if fraction in partition:
            return partition[fraction]
    return []



def main():
    # val = Fraction(2,3,1)
    # val_2 = Fraction(2,3,1)
    # val_3 = Fraction(5,2,1)
    # hashed = hash(val)
    # hashed_2 = hash(val_2)
    # hashed_3 = hash(val_3)
    # print(hashed)
    # print(hashed_2)
    # print(hashed_3)
    fraction_list = [Fraction(-1,4,1), Fraction(1,2,3), Fraction(1,4,6)]
    print(unique_sorted_list(fraction_list))


if __name__ == "__main__":
    main()