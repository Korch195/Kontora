import unittest
from gpt_solution import Rational

class TestRational(unittest.TestCase):
    def test_creation(self):
        rational = Rational(3, 4)
        self.assertEqual(rational.numerator, 3)
        self.assertEqual(rational.denominator, 4)

    def test_str_representation(self):
        rational = Rational(3, 4)
        self.assertEqual(str(rational), "3/4")

    def test_gcd_method(self):
        rational = Rational(6, 8)
        self.assertEqual(rational._gcd(6, 8), 2)

    def test_mixed_form_property(self):
        rational = Rational(5, 4)
        self.assertEqual(rational.mixed_form, "1 1/4")

    def test_mixed_form_setter(self):
        rational = Rational(5, 4)
        rational.mixed_form = "2 3/4"
        self.assertEqual(rational.numerator, 11)
        self.assertEqual(rational.denominator, 4)

        rational.mixed_form = "2/3"
        self.assertEqual(rational.numerator, 2)
        self.assertEqual(rational.denominator, 3)

    def test_reduce_method(self):
        rational = Rational(6, 8)
        reduced_rational = rational.reduce()
        self.assertEqual(reduced_rational.numerator, 3)
        self.assertEqual(reduced_rational.denominator, 4)

    def test_addition(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(1, 4)
        result = rational1 + rational2
        self.assertEqual(str(result), "3/4")

    def test_subtraction(self):
        rational1 = Rational(3, 4)
        rational2 = Rational(1, 4)
        result = rational1 - rational2
        self.assertEqual(str(result), "1/2")

    def test_multiplication(self):
        rational1 = Rational(1, 2)
        rational2 = Rational(3, 4)
        result = rational1 * rational2
        self.assertEqual(str(result), "3/8")

    def test_division(self):
        rational1 = Rational(3, 4)
        rational2 = Rational(1, 2)
        result = rational1 / rational2
        self.assertEqual(str(result), "3/2")

    def test_equality(self):
        rational1 = Rational(3, 4)
        rational2 = Rational(6, 8)
        self.assertEqual(rational1, rational2)

    def test_less_than(self):
        rational1 = Rational(1, 4)
        rational2 = Rational(1, 2)
        self.assertTrue(rational1 < rational2)

    def test_less_than_or_equal(self):
        rational1 = Rational(1, 4)
        rational2 = Rational(1, 4)
        self.assertTrue(rational1 <= rational2)

    def test_invalid_denominator(self):
        with self.assertRaises(ValueError):
            Rational(1, 0)

    def test_invalid_mixed_form_denominator_zero(self):
        rational = Rational(1, 2)
        with self.assertRaises(ValueError):
            rational.mixed_form = "1/0"

    def test_negative_value(self):
        rational = Rational(-3, 4)
        self.assertEqual(str(rational), "-3/4")

    def test_mixed_form_negative(self):
        rational = Rational(-5, 4)
        self.assertEqual(rational.mixed_form, "-1 1/4")

    def test_mixed_form_negative_numerator(self):
        rational = Rational(-5, 4)
        rational.mixed_form = "-2 1/4"
        self.assertEqual(str(rational), "-9/4")

    def test_invalid_mixed_form_format(self):
        rational = Rational(3, 4)
        with self.assertRaises(ValueError) as context:
            rational.mixed_form = "form"
        self.assertEqual(str(context.exception), "Invalid mixed form format.")

    def test_denominator_negative(self):
        rational = Rational(1, -4)
        self.assertEqual(str(rational), "-1/4")

    def test_denominator_negative_mixed_form(self):
        rational = Rational(3, -4)
        self.assertEqual(rational.mixed_form, "-3/4")

    def test_mixed_form_setter_invalid_denominator(self):
        # Test case where value does not contain a space and denominator is zero
        rational = Rational(5, 4)
        with self.assertRaises(ValueError):
            rational.mixed_form = "2/0"

    def test_mixed_form_setter_with_mixed_form(self):
        # Test case where value contains a space (mixed form)
        rational = Rational(5, 4)
        rational.mixed_form = "2 1/3"
        self.assertEqual(rational.numerator, 7)
        self.assertEqual(rational.denominator, 3)

    def test_mixed_form_setter_with_mixed_form_invalid_denominator(self):
        # Test case where value contains a space (mixed form) and denominator is zero
        rational = Rational(5, 4)
        with self.assertRaises(ValueError):
            rational.mixed_form = "2 1/0"
    
    def test_mixed_form_zero_numerator(self):
    # Test case where numerator is zero
        rational = Rational(0, 4)
        self.assertEqual(rational.mixed_form, "0")

# if __name__ == '__main__':
#     unittest.main()