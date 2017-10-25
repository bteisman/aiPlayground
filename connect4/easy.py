from board import board
from random import randint

class easy:
	def ai(self, board):
		return randint(0, board.colSize)