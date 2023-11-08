import unittest
import logic



class TestLogic(unittest.TestCase):

    def test_check_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.check_winner(board), 'X')
    
    def test_get_empty_board(self):
        expected_board = [
            [None, None, None], 
            [None, None, None], 
            [None, None, None]
            ]
        self.assertEqual(logic.get_empty_board(), expected_board)

if __name__ == '__main__':
    unittest.main()