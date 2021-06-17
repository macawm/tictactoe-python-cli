import unittest
import ttt


class TestGameBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.size = 3
        self.p1 = ttt.GamePlayer('a', 'a')
        self.p2 = ttt.GamePlayer('b', 'b')
        self.board = ttt.GameBoard(self.size, self.p1, self.p2)

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
            self.board.update(i+1, self.p1)

        for i in range(self.size**2):
            self.assertFalse(self.board.square_is_open(i+1))

    def test_allowedMoves(self):
        self.assertEqual(self.size * self.size, self.board.allowed_moves())

    def test_update(self):
        self.board.update(1, self.p1)
        self.assertEqual(self.p1.marker, self.board.mark_at_square(1))
        self.board.update(5, self.p2)
        self.assertEqual(self.p2.marker, self.board.mark_at_square(5))

        self.board.update(10, self.p1)
        self.assertEqual(None, self.board.mark_at_square(10))

    def test_getWinnerNone(self):
        self.assertEqual(None, self.board.get_winner(self.p1))
        self.assertEqual(None, self.board.get_winner(self.p2))

    def test_getWinnerAcross(self):
        for i in range(self.size):
            self.board.update(i*self.size+1, self.p1)
            self.board.update(i*self.size+2, self.p1)
            self.board.update(i*self.size+3, self.p1)
            self.assertTrue(self.p1, self.board.get_winner(self.p1))

    def test_getWinnerDown(self):
        for i in range(self.size):
            self.board.update(i+self.size*1, self.p1)
            self.board.update(i+self.size*2, self.p1)
            self.board.update(i+self.size*3, self.p1)
            self.assertTrue(self.p1, self.board.get_winner(self.p1))

    def test_getWinnerDiagonals(self):
        self.board.update(1, self.p1)
        self.board.update(5, self.p1)
        self.board.update(9, self.p1)
        self.assertTrue(self.p1, self.board.get_winner(self.p1))

        self.board.update(3, self.p2)
        self.board.update(5, self.p2)
        self.board.update(7, self.p2)
        self.assertTrue(self.p2, self.board.get_winner(self.p2))

    def test_getWinnerCat(self):
        self.board.update(1, self.p1)
        self.board.update(2, self.p2)
        self.board.update(3, self.p1)
        self.board.update(4, self.p1)
        self.board.update(5, self.p2)
        self.board.update(6, self.p1)
        self.board.update(7, self.p2)
        self.board.update(8, self.p1)
        self.board.update(9, self.p2)
        self.assertEqual(None, self.board.get_winner(self.p1))
        self.assertEqual(None, self.board.get_winner(self.p2))


class TestGamePlayer(unittest.TestCase):
    def test_player(self):
        p = ttt.GamePlayer('a', 'x')
        self.assertEqual('a', p.name)
        self.assertEqual('x', p.marker)

        p.name = 'b'
        p.marker = 'y'

        self.assertEqual('b', p.name)
        self.assertEqual('y', p.marker)


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ttt.Game()


if __name__ == '__main__':
    unittest.main()
