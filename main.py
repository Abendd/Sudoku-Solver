
def isSafe(board,row,col,value):
	for i in range(9):
		if i!=col:
			if board[row][i]==value:
				return False

	for i in range(9):
		if i!=row:
			if board[i][col]==value:
				return False
	for i in range((row//3)*3,(row//3)*3+3):
		for j in range((col//3)*3,(row//3)*3+3):
			if i==row and j==col:
				continue
			if board[i][j]==value:
				return False
	return True

def nextEmpty(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				return i,j
	return None
def solve(board):
	if nextEmpty(board):
		return True
	else:
		r,c = nextEmpty
	print('a:',board[0][0])
	for i in range(1,10):
		if isSafe(board,r,c,i):
			board[r][c]=i

			if solve(board):
				return True
			board[r][c]=0
	return False

def solveBoard():
	board = [
		 [0,0,0,0,8,0,0,0,0],
		 [8,0,9,0,7,1,0,2,0],
		 [4,0,3,5,0,0,0,0,1],
		 [0,0,0,1,0,0,0,0,7],
		 [0,0,2,0,3,4,0,8,0],
		 [7,3,0,0,0,9,0,0,4],
		 [9,0,0,0,0,0,7,0,2],
		 [0,0,8,2,0,5,0,9,0],
		 [1,0,0,0,4,0,3,0,0]
		]

	board = solve(board,0,0)

	for i in board:
		print(i)




board = [
	 [0,0,0,0,8,0,0,0,0],
	 [8,0,9,0,7,1,0,2,0],
	 [4,0,3,5,0,0,0,0,1],
	 [0,0,0,1,0,0,0,0,7],
	 [0,0,2,0,3,4,0,8,0],
	 [7,3,0,0,0,9,0,0,4],
	 [9,0,0,0,0,0,7,0,2],
	 [0,0,8,2,0,5,0,9,0],
	 [1,0,0,0,4,0,3,0,0]
	]

solve(board)

for i in board:
	print(i)