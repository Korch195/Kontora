import unittest
from working_code2 import Rational

class TestRational(unittest.TestCase):
    def test_creation(self):
        """Test Rational object creation."""
        rational = Rational(3, 4)
        self.assertEqual(rational.numerator, 3)
        self.assertEqual(rational.denominator, 4)

    def test_str_representation(self):
        """Test string representation of Rational."""
        rational = Rational(3, 4)
        self.assertEqual(str(rational), "3/4")

    def test_gcd_method(self):
        """Test _gcd method."""
        rational = Rational(6, 8)
        self.assertEqual(rational._gcd(6, 8), 2)

    def test_mixed_form_property(self):
        """Test mixed_form property."""
        rational = Rational(5, 4)
        self.assertEqual(rational.mixed_form, "1 1/4")

    def test_mixed_form_setter(self):
        """Test mixed_form setter."""
        rational = Rational(5, 4)
        rational.mixed_form = "2 3/4"
        self.assertEqual(rational.numerator, 11)
        self.assertEqual(rational.denominator, 4)

        rational.mixed_form = "2/3"
        self.assertEqual(rational.numerator, 2)
        self.assertEqual(rational.denominator, 3)

    def test_reduce_method(self):
        """Test reduce method."""
        rational = Rational(6, 8)
        reduced_rational = rational.reduce()
        self.assertEqual(reduced_rational.numerator, 3)
        self.assertEqual(reduced_rational.denominator, 4)

    # Add more test cases following the same pattern...

    def test_mixed_form_zero_numerator(self):
        """Test mixed_form property when numerator is zero."""
        rational = Rational(0, 4)
        self.assertEqual(rational.mixed_form, "0")

if __name__ == '__main__':
    unittest.main()