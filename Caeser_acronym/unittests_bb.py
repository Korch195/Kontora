import unittest
from working_code import create_acronym, caesar_encode, caesar_decode  # replace 'your_module' with the actual module name

class TestCreateAcronym(unittest.TestCase):
    def test_create_acronym(self):
        self.assertEqual(create_acronym("random access memory"), "RAM - random access memory")
        self.assertEqual(create_acronym("hello world\npython is fun"), "HW - hello world\nPIF - python is fun")
        self.assertEqual(create_acronym(""), "")
        self.assertIsNone(create_acronym(123))  # test non-string input
        self.assertIsNone(create_acronym("123"))  # test digit in input string

class TestCaesarEncode(unittest.TestCase):
    def test_caesar_encode(self):
        self.assertEqual(caesar_encode('computer', 3), 'frpsxwhu')
        self.assertEqual(caesar_encode('zyra', 2), 'batc')
        self.assertEqual(caesar_encode('cute', 9), 'ldcn')
        self.assertEqual(caesar_encode('hello world', 1), 'ifmmp xpsme')
        self.assertEqual(caesar_encode('', 5), '')

class TestCaesarDecode(unittest.TestCase):
    def test_caesar_decode(self):
        self.assertEqual(caesar_decode('frpsxwhu', 3), 'computer')
        self.assertEqual(caesar_decode('batc', 2), 'zyra')
        self.assertEqual(caesar_decode('ldcn', 9), 'cute')
        self.assertEqual(caesar_decode('ifmmp xpsme', 1), 'hello world')
        self.assertEqual(caesar_decode('', 5), '')

if __name__ == '__main__':
    unittest.main()