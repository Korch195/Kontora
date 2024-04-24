import unittest
from working_code import create_acronym, caesar_encode, caesar_decode

class TestCreateAcronym(unittest.TestCase):
    def test_create_acronym_valid_input(self):
        self.assertEqual(create_acronym("random access memory"), "RAM - random access memory")

    def test_create_acronym_empty_input(self):
        self.assertEqual(create_acronym(""), "")

    def test_create_acronym_invalid_input(self):
        self.assertIsNone(create_acronym(123))
        self.assertIsNone(create_acronym(None))
    
    def test_create_acronym_with_digits(self):
        self.assertIsNone(create_acronym("123"))
        self.assertIsNone(create_acronym("random 123"))

class TestCaesarEncode(unittest.TestCase):
    def test_caesar_encode_valid_input(self):
        self.assertEqual(caesar_encode('computer', 3), 'frpsxwhu')
        self.assertEqual(caesar_encode('zyra', 2), 'batc')
        self.assertEqual(caesar_encode('cute', 9), 'ldcn')

    def test_caesar_encode_with_spaces(self):
        self.assertEqual(caesar_encode('com puter', 3), 'frp sxwhu')
        self.assertEqual(caesar_encode('cute ', 9), 'ldcn ')

class TestCaesarDecode(unittest.TestCase):
    def test_caesar_decode_valid_input(self):
        self.assertEqual(caesar_decode('frpsxwhu', 3), 'computer')
        self.assertEqual(caesar_decode('batc', 2), 'zyra')
        self.assertEqual(caesar_decode('ldcn', 9), 'cute')

    def test_caesar_decode_with_spaces(self):
        self.assertEqual(caesar_decode('frp sxwhu', 3), 'com puter')
        self.assertEqual(caesar_decode('ldcn ', 9), 'cute ')

if __name__ == '__main__':
    unittest.main()
