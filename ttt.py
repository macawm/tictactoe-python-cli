# Tic-Tac-Toe

winner = -1
board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
turn = 0
maxMoves = 9

def printIntro():
	print("Tic-Tac-Toe Game")

def startGame():
	currentMove = 0
	while winner == -1 and currentMove < maxMoves:
		takeTurn()
		checkForWin()
		printBoard()
		currentMove += 1

def takeTurn():
	pass

def checkForWin():
	pass

def printBoard():
	print(board)

def main():
	printIntro()
	startGame()

if __name__ == '__main__':
	main()