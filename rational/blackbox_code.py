""" Rational """
from math import gcd, modf

class Rational:
    """Rational number class"""

    def __init__(self, numerator: int, denominator: int):
        """
        Initialize the rational number
        :param numerator: the numerator of the rational number
        :param denominator: the denominator of the rational number
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._mixed_form = None

    def _reduce(self):
        """
        Reduce the rational number to its simplest form
        :return: a tuple of the reduced numerator and denominator
        """
        div = gcd(self.numerator, self.denominator)
        return self.numerator // div, self.denominator // div

    @property
    def mixed_form(self):
        """
        Get the mixed form of the rational number
        :return: the mixed form of the rational number as a string
        """
        if self._mixed_form is None:
            self._mixed_form = self._to_mixed_form()
        return self._mixed_form

    @mixed_form.setter
    def mixed_form(self, value):
        """
        Set the mixed form of the rational number
        :param value: the mixed form of the rational number as a string
        """
        if value:
            parts = value.split() if len(value) >= 5 else value.split("/")
            if len(parts) == 1:
                self.numerator = int(parts[0])
                self.denominator = 1
            else:
                self.denominator = abs(int(parts[-1]))
                self.numerator = int(parts[0]) if len(parts) == 2 else int(parts[0]) * self.denominator + int(parts[2])
            self._mixed_form = value

    def _to_mixed_form(self):
        """
        Convert the rational number to its mixed form
        :return: the mixed form of the rational number as a string
        """
        whole, frac = modf(abs(self.numerator) / abs(self.denominator))
        if frac == 0.0:
            return str(int(whole))
        if self.numerator < 0 or self.denominator < 0:
            return f"-{int(whole)} {abs(frac):.1f}*{abs(self.denominator)}"
        return f"{int(whole)} {abs(frac):.1f}*{abs(self.denominator)}"

    def __new__(cls, numerator: int = 0, denominator: int = 1):
        """
        Create a new Rational object with the given numerator and denominator
        :param numerator: the numerator of the rational number
        :param denominator: the denominator of the rational number
        :return: a new Rational object
        """
        obj = super().__new__(cls)
        obj.numerator = numerator
        obj.denominator = denominator
        return obj

    def __reduce__(self):
        """
        Reduce the rational number to its simplest form
        :return: a tuple of the reduced numerator and denominator
        """
        return self._reduce()

    def __add__(self, other):
        """
        Add two rational numbers
        :param other: the other rational number
        :return: the sum of the two rational numbers
        """
        if isinstance(other, Rational):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        return NotImplemented

    def __sub__(self, other):
        """
        Subtract two rational numbers
        :param other: the other rational number
        :return: the difference of the two rational numbers
        """
        if isinstance(other, Rational):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        return NotImplemented

    def __mul__(self, other):
        """
        Multiply two rational numbers
        :param other: the other rational number
        :return: the product of the two rational numbers
        """
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        return NotImplemented

    def __truediv__(self, other):
        """
        Divide two rational numbers
        :param other: the other rational number
        :return: the quotient of the two rational numbers
        """
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Division by zero.")
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return Rational(num, den)
        return NotImplemented

    def __eq__(self, other):
        """
        Check if two rational numbers are equal
        :param other: the other rational number
        :return: True if the two rational numbers are equal, otherwise False
        """
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented

    def __lt__(self, other):
        """
        Check if the first rational number is less than the second
        :param other: the other rational number
        :return: True if the first rational number is less than the second, otherwise False
        """
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator) > 0
        return NotImplemented

    def __gt__(self, other):
        """
        Check if the first rational number is greater than the second
        :param other: the other rational number
        :return: True if the first rational number is greater than the second, otherwise False
        """
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator) < 0
        return NotImplemented

    def __ge__(self, other):
        """
        Check if the first rational number is greater than or equal to the second
        :param other: the other rational number
        :return: True if the first rational number is greater than or equal to the second, otherwise False
        """
        if isinstance(other, Rational):
            return self.numerator * other.denominator - self.denominator * other.numerator >= 0
        return NotImplemented

    def __le__(self, other):
        """
        Check if the first rational number is less than or equal to the second
        :param other: the other rational number
        :return: True if the first rational number is less than or equal to the second, otherwise False
        """
        if isinstance(other, Rational):
            return self.numerator * other.denominator - self.denominator * other.numerator <= 0
        return NotImplemented

    def __float__(self):
        """
        Convert the rational number to a float
        :return: the float value of the rational number
        """
        return self.numerator / self.denominator

    def __str__(self):
        """
        Convert the rational number to a string
        :return: the string representation of the rational number
        """
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        """
        Represent the rational number as a string
        :return: the string representation of the rational number
        """
        return "Rational(" + str(self.numerator) + ", " + str(self.denominator) + ")"
