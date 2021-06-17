# Tic-Tac-Toe

XX = "X"
OO = "O"

GS_NOT_DONE = -1
GS_CAT = 0
GS_XWIN = 1
GS_OWIN = 2

def printIntro():
	print("Tic-Tac-Toe Game")
	print("q to quit\n")

def signOff():
	print("Thanks for playing.")

def startGame() -> None:
	global XX,OO
	global GS_CAT,GS_OWIN,GS_XWIN,GS_NOT_DONE

	maxMoves = 9
	gameState = GS_NOT_DONE

	helpBoard = [1,2,3,4,5,6,7,8,9]
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

	currentMove = 0
	printBoard(helpBoard, GS_NOT_DONE)

	while gameState == GS_NOT_DONE:
		takeTurn(board, currentMove)

		if (isXsTurn(currentMove)):
			gameState = GS_XWIN if checkForWin(board, XX) else GS_NOT_DONE
		else:
			gameState = GS_OWIN if checkForWin(board, OO) else GS_NOT_DONE

		currentMove += 1

		if (currentMove == maxMoves and not (gameState == GS_XWIN or gameState == GS_OWIN)):
			gameState = GS_CAT

		printBoard(board, gameState)

	signOff()

def takeTurn(board: list, move: int) -> int:
	newMark = getUserInput(board, move)
	updateBoard(board, newMark, move)
	return newMark

def getUserInput(board: list, move: int) -> int:
	badInput = True
	while (badInput):
		square = getPlayerInput(move)
		
		if (square.isdigit()):
			sInt = int(square)
			if (not squareInRange(sInt) or not squareIsOpen(board, sInt)):
				square = handleBadInput()
			else:
				badInput = False
		elif (square == 'q'):
			quit()
		else:
			square = handleBadInput()

	return sInt

def getPlayerInput(move: int) -> str:
	player = XX
	if (not isXsTurn(move)):
		player = OO

	return input("%s make your move. " % player)

def handleBadInput() -> bool:
	print("Bad selection. Try again.")
	return True

def updateBoard(board: list, s: int, move: int):
	global XX,OO
	board[s-1] = XX if isXsTurn(move) else OO

def isXsTurn(currentMove: int) -> bool:
	return currentMove % 2 == 0

def squareInRange(s: int) -> bool:
	return s >= 1 and s <= 9

def squareIsOpen(board: list, s: int) -> bool:
	global XX,OO
	return board[s-1] not in (XX,OO)

def checkForWin(board: list, player: str) -> bool:
	win = False

	for bi in range(3):
		win = win or (board[bi*3] == player and board[bi*3+1] == player and board[bi*3+2] == player)
		win = win or (board[bi] == player and board[bi+3] == player and board[bi+6] == player)

	bi = 0
	#diag l
	win = win or (board[bi] == player and board[bi+4] == player and board[bi+8] == player)
	
	bi = 8
	#diag r
	win = win or (board[bi] == player and board[bi-4] == player and board[bi-8] == player)

	return win

def printBoard(board: list, gameState: int):
	global GS_CAT,GS_OWIN,GS_XWIN

	bi = 0
	print("   %s|%s|%s" %(board[bi],board[bi+1],board[bi+2]))
	print("   -----")
	bi += 3
	print("   %s|%s|%s" %(board[bi],board[bi+1],board[bi+2]))
	print("   -----")
	bi += 3
	print("   %s|%s|%s" %(board[bi],board[bi+1],board[bi+2]))
	print()

	if (gameState == GS_XWIN or gameState == GS_OWIN):
		print("%s Win!!!" % ("Xs" if (gameState == GS_XWIN) else "Os"))
	elif (gameState == GS_CAT):
		print("Cat's game")

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
		self.size = size
		self.__helpInfo = [i for i in range(1, size**2 + 1)]
		self.__data = [' ' for _ in range(size**2)]

	def print_help(self):
		self.print_board(self.__helpInfo, GameState.NOT_DONE)

	def print_board(self, board: list, state: GameState):
		bi = 0
		print("   %s|%s|%s" % (board[bi], board[bi+1], board[bi+2]))
		print("   -----")
		bi += 3
		print("   %s|%s|%s" % (board[bi], board[bi+1], board[bi+2]))
		print("   -----")
		bi += 3
		print("   %s|%s|%s" % (board[bi], board[bi+1], board[bi+2]))
		print()

		if state == GameState.X_WIN or state == GameState.O_WIN:
			print("%s Win!!!" % ("Xs" if (state == GameState.X_WIN) else "Os"))
		elif state == GameState.CAT:
			print("Cat's game")


class GamePlayer:
	def __init__(self, name: str, marker: str):
		self.__name = name
		self.__marker = marker


class Game:
	__state = None

	def __init__(self):
		self.__board = GameBoard(3)
		self.__xPlayer = GamePlayer('Player 1', 'X')
		self.__yPlayer = GamePlayer('Player 2', 'O')

	def start(self):
		self.print_intro()
		self.__state = GameState.NOT_DONE

	def print_intro(self):
		print("Tic-Tac-Toe Game (%s x %s)" % (self.__board.size, self.__board.size))
		print("q to quit\n")
		self.__board.print_help()


if __name__ == '__main__':
	main()
