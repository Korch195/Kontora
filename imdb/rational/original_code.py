""" Rational """
from math import gcd
class Rational:
    """ Rational """
    def __init__(self, numerator, denominator):
        """ Initialize the rational"""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.mixed_form = None
    def reduce(self):
        """ Reduce the rational number"""
        div = gcd(self.numerator, self.denominator)
        return Rational(self.numerator// div, self.denominator//div)
    @property
    def mixed_form(self):
        """ mixed form property """
        whole_part = abs(self.numerator) // abs(self.denominator)
        remainder = abs(self.numerator) % abs(self.denominator)
        if remainder == 0:
            return str(whole_part)
        if self.numerator < 0 or self.denominator<0:
            return f"-{whole_part} {abs(remainder)}/{abs(self.denominator)}"
        return f"{whole_part} {abs(remainder)}/{abs(self.denominator)}"

    @mixed_form.setter
    def mixed_form(self, value):
        """ mixed form setter """
        if value:
            if len(value)< 5:
                part = value.split("/")
                self.denominator = int(part[1])
                self.numerator = int(part[0])
            else:
                if value[0] == "-":
                    parts = value.split()
                    whole = int(parts[0])#2
                    drib = parts[1].split("/")
                    denominator = int(drib[1]) #5
                    nominator = int(drib[0]) #3
                    self.denominator = abs(denominator)
                    self.numerator = (whole)*denominator - abs(nominator)
                else:
                    parts = value.split()
                    whole = int(parts[0])#2
                    drib = parts[1].split("/")
                    denominator = int(drib[1]) #5
                    nominator = int(drib[0]) #3
                    self.denominator = abs(denominator)
                    self.numerator =abs(whole*denominator) + abs(nominator)
    def __add__(self, other):
        """ add """
        if other.numerator == 0:
            return Rational(self.numerator, self.denominator)
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator* other.denominator
        return Rational(new_numerator, new_denominator).reduce()
    def __sub__(self, other):
        """ subtracks """
        if other.numerator == 0:
            return Rational(self.numerator, self.denominator)
        new_numerator =  self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator* other.denominator
        return Rational(new_numerator, new_denominator).reduce()
    def __mul__(self, other):
        """ multiplie """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce()
    def __truediv__(self, other):
        """ truediv """
        if other.numerator == 0 :
             raise ValueError("Denominator cannot be zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).reduce()
    def __eq__(self, other):
        """ check """
        return self.reduce().__dict__ == other.reduce().__dict__
    def __lt__(self, other):
        """ check """
        if self.denominator == other.denominator:
            return self.numerator < other.numerator
        first_n = self.numerator*other.denominator
        second_n= other.numerator * self.denominator
        return first_n < second_n
    def __gt__(self, other):
        """ check """
        if other.numerator == 0:
            return self.numerator > 0
        if self.denominator == other.denominator:
            return self.numerator > other.numerator
        first_n = self.numerator*other.denominator
        second_n= other.numerator * self.denominator
        return first_n > second_n
    def __ge__(self, other):
        """ check """
        if other.numerator == 0:
            return self.numerator >= 0
        if self.denominator == other.denominator:
            return self.numerator >= other.numerator
        first_n = self.numerator*other.denominator
        second_n = other.numerator * self.denominator
        return first_n >= second_n
    def __le__(self, other):
        """ check """
        if self.denominator == other.denominator:
            return self.numerator <= other.numerator
        first_n = self.numerator*other.denominator
        second_n = other.numerator * self.denominator
        return first_n <= second_n
    def __str__(self):
        """ return the string form """
        if self.numerator == 0:
            return f"{self.numerator}/{abs(self.denominator)}"
        if self.numerator < 0 and self.denominator<0:
            return f"{abs(self.numerator)}/{abs(self.denominator)}"
        if self.numerator<0 or self.denominator<0:
            return f"-{abs(self.numerator)}/{abs(self.denominator)}"
        return f"{self.numerator}/{self.denominator}"
