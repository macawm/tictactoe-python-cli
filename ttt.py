# Tic-Tac-Toe

winner = -1
board = [1,2,3,4,5,6,7,8,9]
turn = 0
maxMoves = 9
XX = 0
YY = 1

def printIntro():
	print("Tic-Tac-Toe Game")

def startGame():
	global winner

	currentMove = 0
	while winner == -1 and currentMove < maxMoves:
		takeTurn()
		currentMove += 1

		xWin = checkForWin(XX)
		print("xWin %s" % xWin) #debug
		yWin = checkForWin(YY)
		print("yWin %s" % yWin) #debug

		winner = xWin or yWin
		printBoard(xWin, yWin, winner and currentMove >= maxMoves)

def takeTurn():
	global turn

	square = -1
	while (square == -1):
		if (turn == 0):
			square = input("X make your move. ")
		else:
			square = input("Y make your move. ")
		
		if (not squareInRange(square) and not squareIsOpen(square)):
			print("Bad selection. Try again.")
			square = -1

	updateBoard(int(square))
	turn = 1 if turn == 0 else 0
	return square


def updateBoard(s):
	board[s] = "X" if turn == 0 else "Y"

def squareInRange(s):
	return isinstance(s,str)

def squareIsOpen(s):
	return board[s] in range(0,9)

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
	print(board[bi:bi+3])
	bi += 3
	print(board[bi:bi+3])
	bi += 3
	print(board[bi:bi+3])
	print("")

	if (xWin or yWin):
		print("%s Wins!!!" % "Xs" if xWin else "Ys")
	elif (gameDone):
		print("Cat's game")

def main():
	printIntro()
	startGame()

if __name__ == '__main__':
	main()