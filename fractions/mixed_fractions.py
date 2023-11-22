class Fraction:
    __slots__ = ['__w','__n', '__d']
    def __init__(self, whole, numerator, denominator):
        self.__w = whole
        self.__n = numerator
        self.__d = denominator

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
        n = imp_n/gcd_val
        d = imp_d/gcd_val

        # If the denominator is negative, multiply both numerator and denominator by -1
        if d < 0:
            d = d * -1
            n = n * -1

        w = imp_n//imp_d
        n = n % d
        
        return Fraction(w, n, d)



def gcd(a, b):  # greatest common divisor
    while b != 0:
        r = a % b
        a = b
        b = r
    return a