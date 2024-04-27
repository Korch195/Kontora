import unittest
from black import Rational

class TestRational(unittest.TestCase):

    def test_init(self):
        r1 = Rational(1, 2)
        self.assertEqual(r1.numerator, 1)
        self.assertEqual(r1.denominator, 2)
        with self.assertRaises(ValueError):
            Rational(1, 0)

    def test_str(self):
        r1 = Rational(1, 2)
        self.assertEqual(str(r1), "1/2")

    def test_gcd(self):
        r1 = Rational(12, 18)
        self.assertEqual(r1._gcd(12, 18), 6)

    def test_mixed_form(self):
        r1 = Rational(5, 2)
        self.assertEqual(r1.mixed_form, "2 1/2")
        r1.mixed_form = "3 1/4"
        self.assertEqual(r1.numerator, 13)
        self.assertEqual(r1.denominator, 4)

        r = Rational(7, 2)
        self.assertEqual(r.mixed_form, "3 1/2")
        r.mixed_form = "2 1/3"
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 3)

        r = Rational(7, 2)
        self.assertEqual(r.mixed_form, "3 1/2")

        r = Rational(-7, 2)
        self.assertEqual(r.mixed_form, "-3 1/2")

        r = Rational(7, -2)
        self.assertEqual(r.mixed_form, "-3 1/2")

        r = Rational(-7, -2)
        self.assertEqual(r.mixed_form, "3 1/2")

    def test_reduce(self):
        r1 = Rational(6, 8)
        r1.reduce()
        self.assertEqual(r1.numerator, 3)
        self.assertEqual(r1.denominator, 4)

    def test_add(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        r3 = r1 + r2
        self.assertEqual(r3.numerator, 5)
        self.assertEqual(r3.denominator, 6)

    def test_sub(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        r3 = r1 - r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 6)

    def test_mul(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        r3 = r1 * r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 6)

    def test_truediv(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        r3 = r1 / r2
        self.assertEqual(r3.numerator, 3)
        self.assertEqual(r3.denominator, 2)

    def test_eq(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 4)
        self.assertTrue(r1 == r2)
        r3 = Rational(1, 3)
        self.assertFalse(r1 == r3)

    def test_lt(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 3)
        self.assertTrue(r1 < r2)
        r3 = Rational

    def test_negative_numerator_mixed_form(self):
        r = Rational(7, 3)
        r.mixed_form = "2 1/3"
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 3)

    def test_negative_denominator(self):
        with self.assertRaises(ValueError):
            Rational(1, -2)

    def test_le(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        r3 = Rational(2, 3)
        r4 = Rational(3, 4)
        r5 = Rational(3, 2)
        self.assertTrue(r1 <= r2)
        self.assertTrue(r2 <= r3)
        self.assertFalse(r3 <= r2)
        self.assertTrue(r4 <= r5)
        self.assertFalse(r5 <= r4)


    def test_set_mixed_form(self):
        r = Rational()
        r.mixed_form = "3 1/2"
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 2)

        r = Rational()
        r.mixed_form = "-3 1/2"
        self.assertEqual(r.numerator, -7)
        self.assertEqual(r.denominator, 2)

        r = Rational()
        r.mixed_form = "3 1/-2"
        self.assertEqual(r.numerator, -7)
        self.assertEqual(r.denominator, 2)

        r = Rational()
        r.mixed_form = "-3 1/-2"
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 2)

    def test_set_mixed_form_with_whole_part(self):
        rational = Rational()
        rational.mixed_form = "3 1/2"
        self.assertEqual(rational.numerator, 7)
        self.assertEqual(rational.denominator, 2)

    def test_set_mixed_form_with_negative_whole_part(self):
        rational = Rational()
        rational.mixed_form = "-3 1/2"
        self.assertEqual(rational.numerator, -7)
        self.assertEqual(rational.denominator, 2)

    def test_set_mixed_form_with_negative_fractional_part(self):
        rational = Rational()
        rational.mixed_form = "3 1/-2"
        self.assertEqual(rational.numerator, -7)
        self.assertEqual(rational.denominator, 2)

    def test_set_mixed_form_with_negative_whole_and_fractional_parts(self):
        rational = Rational()
        rational.mixed_form = "-3 -1/2"
        self.assertEqual(rational.numerator, -5)
        self.assertEqual(rational.denominator, 2)

    def test_mixed_form_setter_no_space(self):
        rational = Rational()
        rational.mixed_form = "3/4"
        self.assertEqual(rational.numerator, 3)
        self.assertEqual(rational.denominator, 4)
    
if __name__ == '__main__':
    unittest.main()