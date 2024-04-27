import unittest

from improved_code import validate_board

class TestAllCases(unittest.TestCase):
    def test_empty_board(self):
        board = [
            "*********",
            "*********",
            "*********",
            "*********",
            "*********",
            "*********",
            "*********",
            "*********",
            "*********"
        ]
        self.assertTrue(validate_board(board))
    
    def test_complete_board(self):
        board = [
            "543678912",
            "678912345",
            "912345678",
            "234567891",
            "567891234",
            "891234567",
            "345789126",
            "789126354",
            "126354798"
        ]
        self.assertFalse(validate_board(board))
    
    def test_invalid_block(self):
        board = [
            "123456789",
            "456789123",
            "789123456",
            "234567891",
            "567891234",
            "891234567",
            "345678912",
            "678912345",
            "912345677"
        ]
        self.assertFalse(validate_board(board))
    
    def test_invalid_column(self):
        board = [
            "123456789",
            "456789123",
            "789123456",
            "234567891",
            "567891234",
            "891234567",
            "345678912",
            "678912345",
            "912345672"
        ]
        self.assertFalse(validate_board(board))
    
    def test_invalid_color_blocks(self):
        board = [
            "123456789",
            "456789123",
            "789123456",
            "234567891",
            "567891234",
            "891234567",
            "345678912",
            "678912345",
            "912345678"
        ]
        self.assertFalse(validate_board(board))

    def test_duplicate_in_row(self):
        board = [
            "123456789",
            "456789123",
            "789123456",
            "234567891",
            "567891234",
            "891234567",
            "345678912",
            "678912345",
            "912345679"
        ]
        self.assertFalse(validate_board(board))
    
    def test_duplicate_in_column(self):
        board = [
            "123456789",
            "456789123",
            "789123456",
            "234567891",
            "567891234",
            "891234567",
            "345678912",
            "678912345",
            "912345678"
        ]
        self.assertFalse(validate_board(board))

    def test_invalid_characters(self):
        board = [
            "123456789",
            "456789123",
            "789123456",
            "234567891",
            "567891234",
            "891234567",
            "345678912",
            "678912345",
            "91234567@"  # Додано неправильний символ
        ]
        self.assertFalse(validate_board(board))

if __name__ == '__main__':
    unittest.main()
