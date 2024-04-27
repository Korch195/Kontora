import unittest
from blackbox_code import calculate_grades


class TestGradeCalculator(unittest.TestCase):
    VALID_INPUTS = [
        ((85, 90, 67, 70, 87), (79.8, 'C')),
        ((97, 93, 84, 78, 80), (86.4, 'B')),
        ((90, 87, 93, 68, 71), (81.8, 'B')),
        ((70, 71, 77, 73, 72), (72.6, 'D')),
        ((90, 89, 92, 87, 91), (89.8, 'B')),
        ((63, 65, 65, 65, 65), (64.6, 'E')),
    ]

    INVALID_INPUTS = [
        ((101, 47, 60, 68, 71), (None, None)),
        ((41, 47, 50, 68, 71), (55.4, 'F')),
        ((0, 0, 0, 0, 0), (0.0, 'F')),
        ((-90, 87, 90, 98, 91), (None, None)),
        ((90, -89, 92, 87, 91), (None, None)),
        ((90, 89, -92, 87, 91), (None, None)),
        ((90, 89, 92, -87, 91), (None, None)),
        ((90, 89, 92, 87, -91), (None, None)),
        ((90, 101, 92, 87, 91), (None, None)),
        ((90, 90, 92, 102, 91), (None, None)),
        ((90, 90, 92, 87, 102), (None, None)),
    ]

    def test_calculate_grades_valid_input(self):
        for input_tuple, expected_tuple in self.VALID_INPUTS:
            self.assertEqual(calculate_grades(input_tuple), expected_tuple)

    def test_calculate_grades_invalid_input(self):
        for input_tuple, expected_tuple in self.INVALID_INPUTS:
            self.assertEqual(calculate_grades(input_tuple), expected_tuple)

    def test_calculate_grades_empty_input(self):
        self.assertEqual(calculate_grades(tuple()), (None, None))

    def test_calculate_grades_single_input(self):
        self.assertEqual(calculate_grades((85,)), (85.0, 'B'))

    def test_calculate_grades_two_inputs(self):
        self.assertEqual(calculate_grades((85, 90)), (87.5, 'B'))

    def test_calculate_grades_three_inputs(self):
        self.assertEqual(calculate_grades((85, 90, 95)), (90.0, 'A'))

    def test_calculate_grades_four_inputs(self):
        self.assertEqual(calculate_grades((85, 90, 95, 100)), (92.5, 'A'))

if __name__ == '__main__':
    unittest.main()