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
        """function returns mixed form """
        if abs(self.numerator) > abs(self.denominator):
            if abs(self.numerator) == self.numerator and abs(self.denominator) == self.denominator:
                first = self.numerator // self.denominator
                second = self.numerator - (self.denominator*first)
                return f"{first} {second}/{self.denominator}"
            first = abs(self.numerator) // abs(self.denominator)
            second = abs(self.numerator) - (abs(self.denominator)*first)
            return f"-{first} {second}/{abs(self.denominator)}"
        if self.numerator == 0:
            return str(0)
        return f"{first} {second}/{self.denominator}"

    @mixed_form.setter
    def mixed_form(self, value):
        """setter for mixed_form property"""
        if ' ' in value:
            first, second = value.split(' ')
            first = int(first)
            if abs(first) == first:
                second_num, denominator = map(int, second.split('/'))
                self.numerator = first * denominator + second_num
                self.denominator = denominator
            else:
                second_num, denominator = map(int, second.split('/'))
                self.numerator = -(abs(first) * denominator + second_num)
                self.denominator = denominator
        else:
            self.numerator, self.denominator = map(int, value.split('/'))

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

    