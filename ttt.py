# Tic-Tac-Toe

def main():
	game = Game()
	game.start()


class GameState:
	def __init__(self):
		pass

	NOT_DONE = -1
	CAT = 0
	X_WIN = 1
	O_WIN = 2


class GameBoard:
	def __init__(self, size: int):
		self.size = 3
		self.__helpInfo = [i for i in range(1, self.size**2 + 1)]
		self.__data = [' ' for _ in range(self.size**2)]

	def print_help(self):
		self.__print_board(self.__helpInfo, GameState.NOT_DONE)

	def print_board(self, state: GameState):
		self.__print_board(self.__data, state)

	def __print_board(self, board: list, state: GameState):
		bi = 0
		print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
		print("   -----")
		bi += 3
		print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
		print("   -----")
		bi += 3
		print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
		print()

		if state == GameState.X_WIN or state == GameState.O_WIN:
			print("%s Win!!!" % ("Xs" if (state == GameState.X_WIN) else "Os"))
		elif state == GameState.CAT:
			print("Cat's game")

	def square_in_range(self, s_int):
		return s_int in range(1, self.size**2 + 1)

	def square_is_open(self, s_int):
		return self.__data[s_int - 1] not in ('X', 'O')

	def allowed_moves(self):
		return self.size**2

	def check_for_win(self, player: str) -> bool:
		win = False

		for bi in range(self.size):
			win = win or (self.__data[bi*3] == player and self.__data[bi*3+1] == player and self.__data[bi*3+2] == player)
			win = win or (self.__data[bi] == player and self.__data[bi+3] == player and self.__data[bi+6] == player)

		bi = 0
		#diag l
		win = win or (self.__data[bi] == player and self.__data[bi+4] == player and self.__data[bi+8] == player)

		bi = 8
		#diag r
		win = win or (self.__data[bi] == player and self.__data[bi-4] == player and self.__data[bi-8] == player)

		return win

	def update(self, new_mark: int, x_turn: bool) -> None:
		self.__data[new_mark-1] = 'X' if x_turn else 'O'


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

			if self.reached_max_moves() and not (self.xWon() or self.oWon()):
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
				if not self.__board.square_in_range(s_int) or not self.__board.square_is_open(s_int):
					bad_input = self.handle_bad_input()
				else:
					bad_input = False
			elif square == 'q':
				quit()
			else:
				bad_input = self.handle_bad_input()

		return s_int

	def get_raw_input(self) -> str:
		player = 'X'
		if not self.is_x_turn():
			player = 'O'

		return input("%s make your move. " % player)

	def is_x_turn(self) -> bool:
		return self.__move % 2 == 0

	def handle_bad_input(self) -> None:
		print("Bad selection. Try again.")
		return True

	def reached_max_moves(self) -> bool:
		return self.__move == self.__board.allowed_moves()

	def xWon(self) -> bool:
		return self.__state == GameState.X_WIN

	def oWon(self) -> bool:
		return self.__state == GameState.O_WIN


if __name__ == '__main__':
	main()
