# Tic-Tac-Toe

winner = -1
board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
turn = 0
maxMoves = 9
XX = 0
YY = 1

def printIntro():
	print("Tic-Tac-Toe Game")

def startGame():
	currentMove = 0
	while winner == -1 and currentMove < maxMoves:
		takeTurn()
		currentMove += 1

		xWin = checkForWin(XX)
		yWin = checkForWin(YY)
		printBoard(xWin, yWin, currentMove >= maxMoves)

def takeTurn():
	pass

def checkForWin(player):
	bi = 0
	#row 1
	win = board[bi] == player and board[bi+1] == player and board[bi+2] == player
	#col 1
	win = win or (board[bi] == player and board[bi+3] == player and board[bi+6] == player)
	bi = 1
	#row 2
	win = win or (board[bi*3] == player and board[bi*3+1] == player and board[bi*3+2] == player)
	#col 2
	win = win or (board[bi] == player and board[bi+3] == player and board[bi+6] == player)
	bi = 2
	#row 3
	win = win or (board[bi*3] == player and board[bi*3+1] == player and board[bi*3+2] == player)
	#col 3
	win = win or (board[bi] == player and board[bi+3] == player and board[bi+6] == player)

	bi = 0
	#diag l
	win = win or (board[bi] == player and board[bi+4] == player and board[bi+8] == player)
	
	bi = 2
	#diag r
	win = win or (board[bi] == player and board[bi+2] == player and board[bi+4] == player)

	return win

def printBoard(xWin, yWin, gameDone):
	bi = 0
	print(board[bi,bi+3])
	bi = 1
	print(board[bi,bi+3])
	bi = 2
	print(board[bi,bi+3])
	if (xWin or yWin):
		print()
		printf("%s Wins!!!", "Xs" if xWin else "Ys")
	elif (gameDone):
		print("Cat's game")

def main():
	printIntro()
	startGame()

if __name__ == '__main__':
	main()