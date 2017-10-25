class board:
	def __init__(self, row, col):
		#change to make board bigger or smaller
		self.rowSize = row
		self.colSize = col

		#board properties
		self.red = 'r'
		self.blue = 'b'
		self.blank = '-'
		self.gameOver = False

		#populate board with blank spaces
		self.b = []
		for i in range(self.rowSize):
			row = []
			for j in range(self.colSize):
				row.append(self.blank)
			self.b.append(row)


	#checks if there is a winner
	def checkGame(self):
		blankCount = 0
		for i in range(self.rowSize):
			for j in range(self.colSize):
				if self.b[i][j] == self.blank:
					blankCount += 1
				if self.checkHorizontal(i, j)[0] or self.checkVertical(i, j)[0] or self.checkDiagonal(i, j)[0]:
					self.gameOver = True
					self.winner = self.findWinner(i, j)
					return
		if blankCount == 0:
			self.gameOver = True
			self.winner = self.blank

	#checks horizontal four, returns True if four in a row found and color found [True, color]
	def checkHorizontal(self, row, col):
		if col + 3 >= self.colSize:
			return [False, self.blank]
		color = self.b[row][col]
		if color == self.blank:
			return [False, self.blank]
		for i in range(col, col+4):
			if self.b[row][i] != color:
				return [False, self.blank]
		return [True, color]

	#checks vertical four downward, returns True if four in a row found and color found [True, color]
	def checkVertical(self, row, col):
		if row + 3 >= self.rowSize:
			return [False, self.blank]
		color = self.b[row][col]
		if color == self.blank:
			return [False, self.blank]
		for i in range(row, row+4):
			if self.b[i][col] != color:
				return [False, self.blank]
		return [True, color]

	#checks diagonal four, returns True if four in a row found and color found [True, color]
	def checkDiagonal(self, row, col):
		left = self.checkDiagonalLeft(row, col)
		right = self.checkDiagonalRight(row, col)
		if left[0]:
			return left
		if right[0]:
			return right
		return [False, self.blank]

	def checkDiagonalLeft(self, row, col):
		if row + 3 >= self.rowSize:
			return [False, self.blank]
		if col - 3 < 0:
			return [False, self.blank]
		color = self.b[row][col]
		if color == self.blank:
			return [False, self.blank]
		for i in range(0, 4):
			if self.b[row+i][col-i] != color:
				return [False, self.blank]
		return [True, color]

	def checkDiagonalRight(self, row, col):
		if row + 3 >= self.rowSize:
			return [False, self.blank]
		if col + 3 >= self.colSize:
			return [False, self.blank]
		color = self.b[row][col]
		if color == self.blank:
			return [False, self.blank]
		for i in range(0, 4):
			if self.b[row+i][col+i] != color:
				return [False, self.blank]
		return [True, color]


	#finds what color won
	def findWinner(self, row, col):
		if self.checkHorizontal(row, col)[1] != '-':
			return self.checkHorizontal(row, col)[1]
		elif self.checkVertical(row, col)[1] != '-':
			return self.checkVertical(row, col)[1]
		else:
			return self.checkDiagonal(row, col)[1]

	#finds what row to drop a disk into for board
	def findRow(self, col):
		for i in range(self.rowSize):
			#return row above non-blank row
			if self.b[i][col] != self.blank:
				return i-1
		return self.rowSize-1

	#updates the board with specific color, returns True if valid
	def updateBoard(self, col, color):
		if col < 0 or col >= self.colSize:
			return False
		if self.findRow(col) != -1:
			self.b[self.findRow(col)][col] = color
			return True
		return False



	def printBoard(self):
		for i in range(self.colSize):
			print i,
		print ""

		for i in self.b:
			for j in i:
				print j,
			print("")














