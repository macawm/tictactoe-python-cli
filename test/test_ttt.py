import unittest
import ttt


class TestGameBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.size = 3
        self.board = ttt.GameBoard(self.size)

    def test_boardSize(self):
        self.assertEqual(self.size, self.board.size)

    def test_boardRange(self):
        for i in range(self.size**2):
            self.assertTrue(self.board.square_in_range(i+1))

    def test_boardOpen(self):
        for i in range(self.size**2):
            self.assertTrue(self.board.square_is_open(i+1))

    def test_boardFull(self):
        for i in range(self.size**2):
            self.board.update(i+1, True)

        for i in range(self.size**2):
            self.assertFalse(self.board.square_is_open(i+1))

    def test_allowedMoves(self):
        self.assertEqual(self.size * self.size, self.board.allowed_moves())

    def test_update(self):
        self.board.update(1, True)
        self.assertEqual('X', self.board.mark_at_square(1))
        self.board.update(5, False)
        self.assertEqual('O', self.board.mark_at_square(5))

        self.board.update(10, True)
        self.assertEqual(None, self.board.mark_at_square(10))


if __name__ == '__main__':
    unittest.main()
