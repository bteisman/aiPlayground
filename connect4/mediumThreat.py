from board import board
from random import randint

'''

Medium ai with slight change to threats

'''
class mediumThreat:
    def ai(self, board, color):
        #finds valid locations
        locations = self.validLocations(board)

        #find three any color three in a row
        pos = self.findLength(board, locations, 3, color)
        if pos != -1:
            return pos

        #find two in a row of your color
        pos = self.findLength(board, locations, 2, color)
        if pos != -1:
            return pos

        #find two in a row of other color
        if color == board.red:
            c = board.blue
        else:
            c = board.red
        pos = self.findLength(board, locations, 2, c)
        if pos != -1:
            return pos

        #find one in a row of your color
        pos = self.findLength(board, locations, 1, color)
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

    def findRow(self, board, col):
        for i in range(board.rowSize):
            #return row above non-blank row
            if board.b[i][col] != board.blank:
                return i-1
        return board.rowSize-1

#Finds three in a row spots-------------------------------------------------------------------------------------------------------------------

    #finds if possible winner or stop opponent from winning, adds threats to this equation so it won't return spot to make opponent win next move
    def findLength(self,board,locations,length,color):
        for i in locations:
            if self.vertical(board, i[0], i[1], length, color): #or self.diagonalLeft(board, i[0], i[1], 3) or self.diagonalRight(board, i[0], i[1], 3):
                #return col
                return i[1]
            h = self.horizontal(board, i[0], i[1], length, color)
            dl = self.diagonalLeft(board, i[0], i[1], length, color)
            dr = self.diagonalRight(board, i[0], i[1], length, color)
            if h[0]:
                if h[1] in locations:
                    return h[1][1]
            if dl[0]:
                if h[1] in locations:
                    return dl[1][1]
            if dr[0]:
                if h[1] in locations:
                    return dr[1][1]
        return -1


#Horizontal checks-------------------------------------------------------------------------------------------------------------------

    #finds horizontal num in a row
    def horizontal(self, board, row, col, num, color):
        for i in range(3, -4, -1):
            if col+i >= 0 and col+i < board.colSize:
                if self.horizontalCheck(board, row, col+i, num, color):
                    return [True, self.horizontalFindBlank(board, row, col+i)]
        return [False, -1]

    def horizontalFindBlank(self, board, row, col):
        for i in range(col, col+4):
            if board.b[row][i] == board.blank:
                return [row, i]
        return -1

    #color as board.blank for either color count of num
    def horizontalCheck(self, board, row, col, num, color):
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
            if color == board.blank or color == board.red:
                return True
        if blueC >= num and redC == 0:
            if color == board.blank or color == board.blue:
                return True
        return False

#Vertical checks-------------------------------------------------------------------------------------------------------------------

    #finds vertical num in a row
    def vertical(self, board, row, col, num, c):
        if row < 0:
            return False
        if row + num >= board.rowSize:
            return False
        color = board.b[row+1][col]
        if color == board.blank:
            return False
        for i in range(row+1, row+num+1):
            if board.b[i][col] != color:
                return False
        if c == board.blank or c == color:
            return True
        return False

#Diagonal Left checks-------------------------------------------------------------------------------------------------------------------

    def diagonalLeft(self, board, row, col, num, color):
        for i in range(3, -4, -1):
            if row+i >= 0 and row+i < board.rowSize and col+i >= 0 and col+i < board.colSize:
                if self.diagonalLeftCheck(board, row+i, col+i, num, color):
                    return [True, self.diagonalLeftFindBlank(board, row+i, col+i)]
        return [False, -1]


    def diagonalLeftFindBlank(self, board, row, col):
        for i in range(4):
            if board.b[row+i][col-i] == board.blank:
                return [row+i, col-i]
        return -1

    def diagonalLeftCheck(self, board, row, col, num, color):
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
            if color == board.blank or color == board.red:
                return True
        if blueC >= num and redC == 0:
            if color == board.blank or color == board.blue:
                return True
        return False


#Diagonal Right checks-------------------------------------------------------------------------------------------------------------------

    #finds diagonal right num in a row
    def diagonalRight(self, board, row, col, num, color):
        for i in range(3, -4, -1):
            if row+i >= 0 and row+i < board.rowSize and col+i >= 0 and col+i < board.colSize:
                if self.diagonalRightCheck(board, row+i, col+i, num, color):
                    return [True, self.diagonalRightFindBlank(board, row+i, col+i)]
        return [False, -1]

    def diagonalRightFindBlank(self, board, row, col):
        for i in range(4):
            if board.b[row+i][col+i] == board.blank:
                return [row+i, col+i]
        return -1

    def diagonalRightCheck(self, board, row, col, num, color):
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
            if color == board.blank or color == board.red:
                return True
        if blueC >= num and redC == 0:
            if color == board.blank or color == board.blue:
                return True
        return False










