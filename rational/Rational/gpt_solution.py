'''
Module for work with rational numbers
'''
class Rational():
    """
    Module for work with rational numbers.
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Initializes a Rational object with the given numerator and denominator.

        Args:
            numerator (int): The numerator of the rational number.
            denominator (int): The denominator of the rational number.

        Raises:
            ValueError: If the denominator is zero.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        if denominator < 0:
            numerator = -numerator
            denominator = abs(denominator)

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """
        Returns the string representation of the rational number.

        Returns:
            str: The string representation of the rational number.
        """
        return f"{self.numerator}/{self.denominator}"

    def _gcd(self, a, b):
        """
        Finds the greatest common divisor of two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The greatest common divisor of the two numbers.
        """
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
        """
        Reduces the rational number to its simplest form.

        Returns:
            Rational: The reduced rational number.
        """
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return Rational(self.numerator,self.denominator)

    def __add__(self, other):
        """
        Adds two rational numbers.

        Args:
            other (Rational): The rational number to add.

        Returns:
            Rational: The sum of the two rational numbers.
        """
        m1 = self.numerator * other.denominator + other.numerator * self.denominator
        m2 = self.denominator * other.denominator
        return Rational(m1, m2).reduce()

    def __sub__(self, other):
        """
        Subtracts a rational number from another.

        Args:
            other (Rational): The rational number to subtract.

        Returns:
            Rational: The difference between the two rational numbers.
        """
        m1 = self.numerator * other.denominator - other.numerator * self.denominator
        m2 = self.denominator * other.denominator
        return Rational(m1, m2).reduce()

    def __mul__(self, other):
        """
        Multiplies two rational numbers.

        Args:
            other (Rational): The rational number to multiply by.

        Returns:
            Rational: The product of the two rational numbers.
        """
        m1 = self.numerator * other.numerator
        m2 = self.denominator * other.denominator
        return Rational(m1, m2).reduce()

    def __truediv__(self, other):
        """
        Divides one rational number by another.

        Args:
            other (Rational): The rational number to divide by.

        Returns:
            Rational: The result of dividing the two rational numbers.
        """
        m1 = self.numerator * other.denominator
        m2 = self.denominator * other.numerator
        return Rational(m1, m2).reduce()

    def __eq__(self, other):
        """
        Checks if two rational numbers are equal.

        Args:
            other (Rational): The rational number to compare.

        Returns:
            bool: True if the two rational numbers are equal, False otherwise.
        """
        return str(self.reduce()) == str(other.reduce())

    def __lt__(self, other):
        """
        Checks if one rational number is less than another.

        Args:
            other (Rational): The rational number to compare.

        Returns:
            bool: True if the first rational number is less than the second, 
            False otherwise.
        """
        ns_numerator = self.numerator * other.denominator
        no_numerator = other.numerator * self.denominator
        return ns_numerator < no_numerator

    def __le__(self, other):
        """
        Checks if one rational number is less than or equal to another.

        Args:
            other (Rational): The rational number to compare.

        Returns:
            bool: True if the first rational number is less than or equal to
            the second, False otherwise.
        """
        ns_numerator = self.numerator * other.denominator
        no_numerator = other.numerator * self.denominator
        return ns_numerator <= no_numerator
        