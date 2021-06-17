# Tic-Tac-Toe

from enum import IntEnum


def main():
	Game().start()


class GameState(IntEnum):
	NOT_DONE = -1
	CAT = 0
	X_WIN = 1
	O_WIN = 2


class GameBoard:
	def __init__(self, size: int):
		self.size = size  # TODO handle different size boards
		self.__helpInfo = [i for i in range(1, self.size**2 + 1)]
		self.__data = [' ' for _ in range(self.size**2)]

	def print_help(self) -> None:
		self.__print_board(self.__helpInfo, GameState.NOT_DONE)

	def print_board(self, state: GameState) -> None:
		self.__print_board(self.__data, state)

	def __print_board(self, board: list, state: GameState) -> None:
		bi = 0
		print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
		print("   -----")
		bi += self.size
		print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
		print("   -----")
		bi += self.size
		print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
		print()

		if state == GameState.X_WIN or state == GameState.O_WIN:
			print("%s Win!!!" % ("Xs" if (state == GameState.X_WIN) else "Os"))
		elif state == GameState.CAT:
			print("Cat's game")

	def square_in_range(self, s_int: int) -> bool:
		return s_int in range(1, self.size**2 + 1)

	def square_is_open(self, s_int: int) -> bool:
		if self.square_in_range(s_int):
			return self.mark_at_square(s_int) not in ('X', 'O')
		else:
			return False

	def allowed_moves(self) -> int:
		return self.size**2

	def check_for_win(self, player: str) -> bool:
		win = False

		for bi in range(self.size):
			win = win or (self.__data[bi*3] == player and self.__data[bi*3+1] == player and self.__data[bi*3+2] == player)
			win = win or (self.__data[bi] == player and self.__data[bi+3] == player and self.__data[bi+6] == player)

		bi = 0
		# diag l
		win = win or (self.__data[bi] == player and self.__data[bi+4] == player and self.__data[bi+8] == player)

		bi = 2
		# diag r
		win = win or (self.__data[bi] == player and self.__data[bi+2] == player and self.__data[bi+4] == player)

		return win

	def update(self, square: int, x_turn: bool) -> None:
		""" This is the first, of only two, places where we alter the user input to correspond with our data store. """
		if self.square_in_range(square):
			self.__data[square - 1] = 'X' if x_turn else 'O'

	def mark_at_square(self, square: int) -> str:
		""" This is the second, of only two, places where we alter the user input to correspond with our data store. """
		if self.square_in_range(square):
			return self.__data[square-1]


class GamePlayer:
	def __init__(self, name: str, marker: str):
		self.__name = name
		self.__marker = marker


class Game:
	__state = None
	__move = None

	def __init__(self):
		self.__board = GameBoard(3)
		self.__xPlayer = GamePlayer('Player 1', 'X')
		self.__yPlayer = GamePlayer('Player 2', 'O')

	def start(self):
		self.print_intro()
		self.__state = GameState.NOT_DONE

		self.__move = 0

		while self.game_not_over():
			self.take_turn()

			if self.is_x_turn():
				self.__state = GameState.X_WIN if self.__board.check_for_win('X') else GameState.NOT_DONE
			else:
				self.__state = GameState.O_WIN if self.__board.check_for_win('O') else GameState.NOT_DONE

			self.__move += 1

			if self.reached_max_moves() and not (self.x_won() or self.o_won()):
				self.__state = GameState.CAT

			self.__board.print_board(self.__state)

	def print_intro(self):
		print("Tic-Tac-Toe Game (%s x %s)" % (self.__board.size, self.__board.size))
		print("q to quit\n")
		self.__board.print_help()

	def game_not_over(self):
		return self.__state == GameState.NOT_DONE

	def take_turn(self) -> int:
		new_mark = self.get_user_input()
		self.__board.update(new_mark, self.is_x_turn())
		return new_mark

	def get_user_input(self) -> int:
		bad_input = True
		while bad_input:
			square = self.get_raw_input()

			if square.isdigit():
				s_int = int(square)
				if not self.__board.square_is_open(s_int):
					print("Bad selection. Try again.")
					bad_input = True
				else:
					bad_input = False
			elif square == 'q':
				quit()
			else:
				print("Bad selection. Try again.")
				bad_input = True

		return s_int

	def get_raw_input(self) -> str:
		player = 'X'
		if not self.is_x_turn():
			player = 'O'

		return input("%s make your move. " % player)

	def is_x_turn(self) -> bool:
		return self.__move % 2 == 0

	def reached_max_moves(self) -> bool:
		return self.__move == self.__board.allowed_moves()

	def x_won(self) -> bool:
		return self.__state == GameState.X_WIN

	def o_won(self) -> bool:
		return self.__state == GameState.O_WIN


if __name__ == '__main__':
	main()
