""" Rational """
from math import gcd
class Rational:
    """A class to represent rational numbers."""

    def __init__(self, numerator, denominator):
        """Initialize Rational with numerator and denominator."""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """Return string representation of the Rational."""
        if self.numerator == 0:
            return f"0/{abs(self.denominator)}"
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Addition of two Rational numbers."""
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce()

    def __sub__(self, other):
        """Subtraction of two Rational numbers."""
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce()

    def __mul__(self, other):
        """Multiplication of two Rational numbers."""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce()

    def __truediv__(self, other):
        """Division of two Rational numbers."""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).reduce()

    def __eq__(self, other):
        """Check if two Rational numbers are equal."""
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __lt__(self, other):
        """Check if self is less than other Rational number."""
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __le__(self, other):
        """Check if self is less than or equal to other Rational number."""
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __gt__(self, other):
        """ Check if self is greater than other """
        if other.numerator == 0:
            return self.numerator > 0
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        """ Check if self is greater than or equal to other """
        if other.numerator == 0:
            return self.numerator >= 0
        return self.numerator * other.denominator >= other.numerator * self.denominator


    def reduce(self):
        """Reduce the Rational number to its simplest form."""
        div = gcd(self.numerator, self.denominator)
        return Rational(self.numerator // div, self.denominator // div)

    @property
    def mixed_form(self):
        """Return the mixed form of the Rational number."""
        sign = '-' if self.numerator * self.denominator < 0 else ''
        whole_part, remainder = divmod(abs(self.numerator), abs(self.denominator))
        if remainder == 0:
            return f"{sign}{whole_part}"
        return f"{sign}{whole_part} {remainder}/{abs(self.denominator)}"



    @mixed_form.setter
    def mixed_form(self, value):
        """Set the Rational number from its mixed form."""
        if value:
            parts = value.split()
            whole = int(parts[0]) if parts[0][0] != '-' else -int(parts[0][1:])
            nominator, denominator = map(int, parts[1].split('/'))
            self.denominator = abs(denominator)
            self.numerator = whole * self.denominator + (-1 if whole < 0 else 1) * abs(nominator)
