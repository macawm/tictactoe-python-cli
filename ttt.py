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
	turn = 0

	currentMove = 0
	printBoard(helpBoard, False, False, False)

	while not winner and currentMove < maxMoves:
		takeTurn(board, turn)
		turn = updateTurn(turn)
		currentMove += 1

		xWin = checkForWin(board, XX)
		#print("xWin %s" % xWin) #debug
		oWin = checkForWin(board, OO)
		#print("oWin %s" % oWin) #debug

		winner = xWin or oWin
		printBoard(board, xWin, oWin, not winner and currentMove == maxMoves)

def takeTurn(board, turn):
	square = -1
	while (square == -1):
		if (turn == 0):
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

	updateBoard(board, sInt-1, turn)
	return square

def handleBadInput():
	print("Bad selection. Try again.")
	return -1

def updateTurn(turn):
	next = 1 if turn == 0 else 0
	return next

def updateBoard(board, s, turn):
	global XX,OO
	board[s] = XX if turn == 0 else OO

def squareInRange(s):
	return s >= 1 and s <= 9

def squareIsOpen(board, s):
	global XX,OO
	return board[s-1] not in (XX,OO)

def checkForWin(board, player):
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