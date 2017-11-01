from board import board

class human:
	def ai(self, board, color):
		col = raw_input("Choose col: ")
		try:
			c = int(col)
		except:
			c = -1
		return c