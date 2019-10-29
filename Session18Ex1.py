#Add methods to overwrite len(),+,-,==,<.

class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __add__(self, other):
        sum_den = self.den * other.den
        sum_num = self.num * other.den + self.den * other.num
        return Fraction(sum_num, sum_den)