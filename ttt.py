# Tic-Tac-Toe

XX = "X"
OO = "O"

def printIntro():
	print("Tic-Tac-Toe Game")
	print("q to quit\n")

def startGame():
	global XX,OO
	maxMoves = 9

	winner = False
	helpBoard = [1,2,3,4,5,6,7,8,9]
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

	currentMove = 0
	printBoard(helpBoard, False, False, False)

	while not winner and currentMove < maxMoves:
		takeTurn(board, currentMove)
		currentMove += 1

		xWin = checkForWin(board, XX)
		oWin = checkForWin(board, OO)

		winner = xWin or oWin
		printBoard(board, xWin, oWin, not winner and currentMove == maxMoves)

def takeTurn(board, move):
	square = -1
	while (square == -1):
		if (isXsTurn(move)):
			square = input(XX + " make your move. ")
		else:
			square = input(OO + " make your move. ")
		
		if (square.isdigit()):
			sInt = int(square)
			if (not squareInRange(sInt) or not squareIsOpen(board, sInt)):
				square = handleBadInput()
		elif (square == 'q'):
			quit()
		else:
			square = handleBadInput()

	updateBoard(board, sInt-1, move)
	return square

def handleBadInput():
	print("Bad selection. Try again.")
	return -1

def updateBoard(board, s, move):
	global XX,OO
	board[s] = XX if isXsTurn(move) else OO

def isXsTurn(currentMove):
	return currentMove %2 == 0

def squareInRange(s):
	return s >= 1 and s <= 9

def squareIsOpen(board, s):
	global XX,OO
	return board[s-1] not in (XX,OO)

def checkForWin(board, player):
	win = False

	for bi in range(3):
		win = win or (board[bi*3] == player and board[bi*3+1] == player and board[bi*3+2] == player)
		win = win or (board[bi] == player and board[bi+3] == player and board[bi+6] == player)

	bi = 0
	#diag l
	win = win or (board[bi] == player and board[bi+4] == player and board[bi+8] == player)
	
	bi = 2
	#diag r
	win = win or (board[bi] == player and board[bi+2] == player and board[bi+4] == player)

	return win

def printBoard(board, xWin, oWin, gameDone):
	bi = 0
	print("   %s|%s|%s" %(board[bi],board[bi+1],board[bi+2]))
	print("   -----")
	bi += 3
	print("   %s|%s|%s" %(board[bi],board[bi+1],board[bi+2]))
	print("   -----")
	bi += 3
	print("   %s|%s|%s" %(board[bi],board[bi+1],board[bi+2]))
	print()

	if (xWin or oWin):
		print("%s Win!!!" % ("Xs" if xWin else "Os"))
	elif (gameDone):
		print("Cat's game")

def main():
	printIntro()
	startGame()

if __name__ == '__main__':
	main()