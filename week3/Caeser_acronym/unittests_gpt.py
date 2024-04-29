import unittest
from working_code import caesar_encode, caesar_decode
from acr_gpt import create_acronym

class TestCreateAcronym(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(create_acronym("random access memory\nAs soon As possible"), "RAM - random access memory\nASAP - As soon As possible")
    def test_invalid_input_with_special_characters(self):
        self.assertIsNone(create_acronym("random @ccess memory\nAs soon As possible"))
    def test_invalid_input_with_numbers(self):
        self.assertIsNone(create_acronym("random access 123\nAs soon As possible"))
    def test_empty_input(self):
        self.assertIsNone(create_acronym(""))
    def test_single_word_input(self):
        self.assertEqual(create_acronym("hello"), "H - hello")
    def test_single_phrase_input(self):
        self.assertEqual(create_acronym("this is a single phrase"), "TIASP - this is a single phrase")
    def test_multiple_phrases_input_with_empty_line_at_end(self):
        self.assertEqual(create_acronym("one\ntwo\nthree\n"), "O - one\nT - two\nT - three")
    def test_multiple_phrases_input_without_empty_line_at_end(self):
        self.assertEqual(create_acronym("one\ntwo\nthree"), "O - one\nT - two\nT - three")
    def test_non_latin_input(self):
        self.assertEqual(create_acronym("Факультет прикладних наук\nУкраїнський Католицький Університет\nЇжачок"), "ФПН - Факультет прикладних наук\nУКУ - Український Католицький Університет\nЇ - Їжачок")
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
