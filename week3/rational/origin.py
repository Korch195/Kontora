'''
This module has a class for a rational numbers
'''
class Rational():
    '''
    This class defines rational numbers
    '''
    def __init__(self, numerator: int, denominator: int):
        '''
        Receives values of parameters
        '''
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        '''
        Returns self
        '''
        return f"{self.numerator}/{self.denominator}"

    def _gcd(self, a, b):
        '''
        Helper function to find greatest common divisor
        '''
        while b:
            a, b = b, a % b
        return a

    @property
    def mixed_form(self):
        '''
        Return rational number in mixed form
        '''
        if self.numerator < 0:
            self.numerator = -self.numerator
            z = -(self.numerator // self.denominator)
            rem = self.numerator % self.denominator
        else:
            z = self.numerator // self.denominator
            rem = self.numerator % self.denominator
        return f"{z} {abs(rem)}/{self.denominator}"

    @mixed_form.setter
    def mixed_form(self, value: str):
        '''
        Add the whole part to the rational number 
        '''
        if ' ' not in value:
            num, den = map(int, value.split('/'))
            self.numerator = num
            self.denominator = den
        else:
            z, fr = value.split(' ')
            num, den = map(int, fr.split('/'))
            if z.startswith('-'):
                num = -num
            z = int(z)
            self.numerator = num + (z * den)
            self.denominator = den

    def reduce(self):
        '''
        Reduces the rational number
        '''
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return Rational(self.numerator,self.denominator)

    def __add__(self, other):
        '''
        Add to rational numbers
        '''
        m1 = self.numerator * other.denominator + other.numerator * self.denominator
        m2 = self.denominator * other.denominator
        rel3 = Rational(m1, m2).reduce()
        return rel3

    def __sub__(self, other):
        '''
        Substract rational numbers
        '''
        m1 = self.numerator * other.denominator - other.numerator * self.denominator
        m2 = self.denominator * other.denominator
        rel3 = Rational(m1, m2).reduce()
        return rel3

    def __mul__(self, other):
        '''
        Multiplies two rational numbers
        '''
        m1 = self.numerator * other.numerator
        m2 = self.denominator * other.denominator
        m3 = Rational(m1, m2).reduce()
        return m3

    def __truediv__(self, other):
        '''
        Divides rational numbers
        '''
        m1 = self.numerator * other.denominator
        m2 = self.denominator * other.numerator
        m3 = Rational(m1, m2).reduce()
        return m3

    def __eq__(self, other):
        '''
        Check whether the rational numbers are equal
        '''
        return str(self.reduce()) == str(other.reduce())

    def __lt__(self, other):
        '''
        Check whether the rational number is less than another rational number.
        '''
        spilne = self.denominator * other.denominator
        ns_numerator = self.numerator * spilne
        no_numerator = other.numerator * spilne
        return ns_numerator < no_numerator

    def __le__(self, other):
        '''
        Check whether the rational number is less than another rational number.
        '''
        spilne = self.denominator * other.denominator
        ns_numerator = self.numerator * spilne
        no_numerator = other.numerator * spilne
        return ns_numerator <= no_numerator

def test_rational():
    """Testing class Rational ..."""
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert rational1.numerator == 1
    assert rational1.denominator == 4
    assert isinstance(rational1, Rational)
    assert str(rational1) == "1/4"

    try:
        rational2 = Rational(1, 0)
    except ValueError as e:
        assert f'{e}' == "Denominator cannot be zero."

    rational2 = Rational(2, 4)
    assert rational2.numerator == 2
    assert rational2.denominator == 4
    assert isinstance(rational2, Rational)
    assert str(rational2) == "2/4"
    rational2 = rational2.reduce()
    assert str(rational2) == "1/2"

    # here you can add two numbers
    rational2 = Rational(2, 5)
    assert str(rational1 + rational2) == "13/20", str(rational1 + rational2)

    # here is a substraction
    assert str(rational1 - rational2) == "-3/20"

    # multiplication
    assert str(rational1 * rational2) == "1/10"

    # division
    assert str(rational1 / rational2) == "5/8"
    assert str(rational1 / rational2*rational1-rational1) == "-3/32"

    rational3 = Rational(2, 8)
    assert str(rational3) == "2/8"

    assert rational1 == rational3

    assert rational1 < rational2

    assert rational1 <= rational2

    assert rational1 <= rational3

    rational3 = Rational(2, -8)
    assert str(rational3) == "-2/8"

    rational4 = Rational(10, 8)
    assert str(rational4) == "10/8"
    assert rational4.mixed_form == "1 2/8"

    rational4.mixed_form = '2 3/5'
    assert str(rational4) == '13/5'
    assert isinstance(rational4, Rational)

    rational4.mixed_form = '3/5'
    assert str(rational4) == '3/5'

    rational5 = Rational(0, -4)
    assert str(rational5) == '0/4'
    assert str(rational5.reduce()) == '0/1'

    rational6 = Rational(10, -8)
    assert str(rational6) == "-10/8"
    assert rational6.mixed_form == "-1 2/8"
    rational7 = Rational(-10, 8)
    assert str(rational7) == "-10/8"
    assert rational7.mixed_form == "-1 2/8"

    rational4.mixed_form = "-1 2/8"
    assert str(rational4) == '-10/8'
    assert rational4.numerator == -10
    assert rational4.denominator == 8
    assert isinstance(rational4, Rational)

    print("Done!")


if __name__ == '__main__':
    test_rational()
    