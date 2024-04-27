from improved_code import validate_board

import unittest

class TestValidateBoard(unittest.TestCase):

    def test_valid_board(self):
        board = [
            "87654321*",
            "28914567*",
            "*13729485",
            "5943178*6",
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*892164"
        ]
        self.assertTrue(validate_board(board))

    def test_duplicate_row(self):
        board = [
            "87654321*",
            "28914567*",
            "*13729485",
            "5943178*6",
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*892164",
            "35*892164"  # duplicate row
        ]
        self.assertFalse(validate_board(board))

    def test_duplicate_column(self):
        board = [
            "87654321*",
            "28914567*",
            "*13729485",
            "5943178*61",  # duplicate column
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*892164"
        ]
        self.assertFalse(validate_board(board))

    def test_duplicate_block(self):
        board = [
            "87654321*",
            "28914567*",
            "*13729485",
            "5943178*6",
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*8921644"  # duplicate block
        ]
        self.assertFalse(validate_board(board))

    def test_out_of_range_row(self):
        board = [
            "87654321*",
            "28914567*",
            "*13729485",
            "5943178*6",
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*892164",
            "057892164"  # out of range row
        ]
        self.assertFalse(validate_board(board))

    def test_out_of_range_column(self):
        board = [
            "87654321*0",  # out of range column
            "28914567*",
            "*13729485",
            "5943178*6",
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*892164"
        ]
        self.assertFalse(validate_board(board))

    def test_invalid_character(self):
        board = [
            "87654321*",
            "28914567@",  # invalid character
            "*13729485",
            "5943178*6",
            "1286795*4",
            "765*31248",
            "93258476*",
            "*81263957",
            "35*892164"
        ]
        self.assertFalse(validate_board(board))

if __name__ == '__main__':
    unittest.main()