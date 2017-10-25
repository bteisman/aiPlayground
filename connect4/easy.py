from board import board
from random import randint

'''

Easy ai

Only checks for possible three in a row combinations and returns that col to put disk in, doesn't check if that would stop 4 in a row
Otherwise chooses random col, no offensive strategy

'''
class easy:
    def ai(self, board):
        locations = self.validLocations(board)
        pos = self.findThree(board, locations)
        if pos != -1:
            return pos
        #returns random col from valid locations on board
        return locations[randint(0, len(locations)-1)][1]


    #returns all possible valid locations
    def validLocations(self, board):
        loc = []
        for col in range(board.colSize):
            found = False
            for row in range(board.rowSize):
                #return row above non-blank row
                if board.b[row][col] != board.blank and not found:
                    if row != -1:
                        found = True
                        loc.append([row-1, col])
            if not found:
                loc.append([board.rowSize-1, col])
        return loc

#Finds three in a row spots-------------------------------------------------------------------------------------------------------------------

    #finds if possible winner or stop opponent from winning
    def findThree(self,board,locations):
        for i in locations:
            if self.vertical(board, i[0], i[1], 3): #or self.diagonalLeft(board, i[0], i[1], 3) or self.diagonalRight(board, i[0], i[1], 3):
                #return col
                return i[1]
            h = self.horizontal(board, i[0], i[1], 3)
            dl = self.diagonalLeft(board, i[0], i[1], 3)
            dr = self.diagonalRight(board, i[0], i[1], 3)
            if h[0]:
                return h[1]
            if dl[0]:
                return dl[1]
            if dr[0]:
                return dr[1]
        return -1

#Horizontal checks-------------------------------------------------------------------------------------------------------------------

    #finds horizontal num in a row
    def horizontal(self, board, row, col, num):
        for i in range(3, -4, -1):
            if col+i >= 0 and col+i < board.colSize:
                if self.horizontalCheck(board, row, col+i, num):
                    return [True, self.horizontalFindBlank(board, row, col+i)]
        return [False, -1]

    def horizontalFindBlank(self, board, row, col):
        for i in range(col, col+4):
            if board.b[row][i] == board.blank:
                return i
        return -1

    def horizontalCheck(self, board, row, col, num):
        if col + 3 >= board.colSize:
            return False
        blankC = 0
        redC = 0
        blueC = 0
        for i in range(4):
            if board.b[row][i+col] == board.blank:
                blankC += 1
            elif board.b[row][i+col] == board.red:
                redC += 1
            else:
                blueC += 1
        if redC >= num and blueC == 0:
            return True
        if blueC >= num and redC == 0:
            return True
        return False

#Vertical checks-------------------------------------------------------------------------------------------------------------------

    #finds vertical num in a row
    def vertical(self, board, row, col, num):
        if row + num >= board.rowSize:
            return False
        color = board.b[row+1][col]
        if color == board.blank:
            return False
        for i in range(row+1, row+num+1):
            if board.b[i][col] != color:
                return False
        return True

#Diagonal Left checks-------------------------------------------------------------------------------------------------------------------

    def diagonalLeft(self, board, row, col, num):
        for i in range(3, -4, -1):
            if row+i >= 0 and row+i < board.rowSize and col+i >= 0 and col+i < board.colSize:
                if self.diagonalLeftCheck(board, row+i, col+i, num):
                    return [True, self.diagonalLeftFindBlank(board, row+i, col+i)]
        return [False, -1]


    def diagonalLeftFindBlank(self, board, row, col):
        for i in range(4):
            if board.b[row+i][col-i] == board.blank:
                return col-i
        return -1

    def diagonalLeftCheck(self, board, row, col, num):
        if row + 3 >= board.rowSize:
            return False
        if col - num < 0:
            return False
        blankC = 0
        redC = 0
        blueC = 0
        for i in range(4):
            if board.b[row+i][col-i] == board.blank:
                blankC += 1
            elif board.b[row+i][col-i] == board.red:
                redC += 1
            else:
                blueC += 1
        if redC >= num and blueC == 0:
            return True
        if blueC >= num and redC == 0:
            return True
        return False


#Diagonal Right checks-------------------------------------------------------------------------------------------------------------------

    #finds diagonal right num in a row
    def diagonalRight(self, board, row, col, num):
        for i in range(3, -4, -1):
            if row+i >= 0 and row+i < board.rowSize and col+i >= 0 and col+i < board.colSize:
                if self.diagonalRightCheck(board, row+i, col+i, num):
                    return [True, self.diagonalRightFindBlank(board, row+i, col+i)]
        return [False, -1]

    def diagonalRightFindBlank(self, board, row, col):
        for i in range(4):
            if board.b[row+i][col+i] == board.blank:
                return col+i
        return -1

    def diagonalRightCheck(self, board, row, col, num):
        if row + 3 >= board.rowSize:
            return False
        if col + 3 >= board.colSize:
            return False
        blankC = 0
        redC = 0
        blueC = 0
        for i in range(4):
            if board.b[row+i][col+i] == board.blank:
                blankC += 1
            elif board.b[row+i][col+i] == board.red:
                redC += 1
            else:
                blueC += 1
        if redC >= num and blueC == 0:
            return True
        if blueC >= num and redC == 0:
            return True
        return False










