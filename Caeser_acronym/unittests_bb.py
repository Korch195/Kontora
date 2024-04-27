import unittest
from working_code import caesar_encode, caesar_decode  # replace 'your_module' with the actual module name
from acr_bb import create_acronym
class TestCreateAcronym(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(create_acronym("random access memory\nAs soon as possible"),
                             "RAM - random access memory\nASAP - As soon as possible")
    
    def test_non_string_input(self):
        self.assertIsNone(create_acronym(123))
    
    def test_empty_last_line(self):
        self.assertEqual(create_acronym("random access memory\nAs soon as possible\n"),
                             "RAM - random access memory\nASAP - As soon as possible")
    
    def test_non_alpha_input(self):
        self.assertIsNone(create_acronym("random access memory 123\nAs soon as possible"))
    
    def test_mixed_case_input(self):
        self.assertEqual(create_acronym("miXed cAse mEssage\nflip Flop"),
                             "MCM - miXed cAse mEssage\nFF - flip Flop")
    
    def test_non_english_input(self):
        self.assertEqual(create_acronym("випадковий доступ до пам'яті\nЯкнайшвидше"),
                             "ВДДП - випадковий доступ до пам'яті\nЯ - Якнайшвидше")
    
    def test_empty_input(self):
        self.assertIsNone(create_acronym(""))
    
    def test_all_uppercase_input(self):
        self.assertEqual(create_acronym("RANDOM ACCESS MEMORY\nAS SOON AS POSSIBLE"),
                             "RAM - RANDOM ACCESS MEMORY\nASAP - AS SOON AS POSSIBLE")

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