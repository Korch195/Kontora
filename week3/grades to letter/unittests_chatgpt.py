import unittest
from chat_gpt_code import calculate_grade

import unittest
from chat_gpt_code import calculate_grade

class TestCalculateGrade(unittest.TestCase):
    def test_valid_grades(self):
        # Testing valid grades with expected outcomes
        self.assertEqual(calculate_grade(85, 90, 67, 70, 87), (79.8, "C"))
        self.assertEqual(calculate_grade(97, 93, 84, 78, 80), (86.4, "B"))
        self.assertEqual(calculate_grade(90, 90, 90, 90, 90), (90.0, "A"))
        self.assertEqual(calculate_grade(60, 60, 60, 60, 60), (60.0, "E"))

    def test_invalid_grades(self):
        # Testing invalid grades (outside the range [0, 100])
        self.assertIsNone(calculate_grade(85, 90, 67, 70, 107))
        self.assertIsNone(calculate_grade(-10, 90, 67, 70, 87))
        self.assertIsNone(calculate_grade(85, 90, 67, 70, -20))

    def test_grade_assignment(self):
        # Testing grade assignment logic
        self.assertEqual(calculate_grade(80, 80, 80, 80, 80), (80.0, "B"))  # Average grade in middle of ranges
        self.assertEqual(calculate_grade(90, 90, 89, 89, 89), (89.4, "B"))  # Average grade at lower bound of A

    def test_letter_grades(self):
        # Testing letter grade assignment
        self.assertEqual(calculate_grade(90, 90, 90, 90, 90), (90.0, "A"))
        self.assertEqual(calculate_grade(85, 85, 85, 85, 85), (85.0, "B"))
        self.assertEqual(calculate_grade(78, 78, 78, 78, 78), (78.0, "C"))
        self.assertEqual(calculate_grade(70, 70, 70, 70, 70), (70.0, "D"))
        self.assertEqual(calculate_grade(62, 62, 62, 62, 62), (62.0, "E"))
        self.assertEqual(calculate_grade(0, 0, 0, 0, 0), (0.0, "F"))

    def test_edge_cases(self):
        # Testing edge cases
        self.assertEqual(calculate_grade(75, 75, 75, 75, 75), (75.0, "C"))  # All grades the same
        self.assertEqual(calculate_grade(79, 79, 79, 79, 79), (79.0, "C"))  # Average on boundary
        self.assertEqual(calculate_grade(90, 90, 90, 90, 89), (89.8, "A"))  # A-/B+ boundary
        self.assertEqual(calculate_grade(80, 80, 80, 80, 79), (79.8, "B"))  # B-/C+ boundary
        self.assertEqual(calculate_grade(0, 0, 0, 0, 1), (1.0, "F"))       # F/D boundary

    def test_non_integer_grades(self):
        # Testing non-integer grades
        self.assertEqual(calculate_grade(85.5, 90.3, 67.8, 70.1, 87.9), (80.3, "B"))
        self.assertEqual(calculate_grade(85.6, 90.9, 67.4, 70.8, 87.2), (80.4, "B"))

if __name__ == "__main__":
    unittest.main()
