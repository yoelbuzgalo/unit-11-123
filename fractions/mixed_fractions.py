class Fraction:
    __slots__ = ['__w','__n', '__d']
    def __init__(self, whole, numerator, denominator):
        self.__w = whole
        self.__n = numerator
        self.__d = denominator

    def get_fraction(self):
        return (self.__w, self.__n, self.__d)

def gcd(a, b):  # greatest common divisor
    while b != 0:
        r = a % b
        a = b
        b = r
    return a