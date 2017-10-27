from board import board
from randobot import randobot
from human import human
from easy import easy
from medium import medium
from mediumPrime import mediumPrime
from mediumThreat import mediumThreat
import sys
#Must import bots here

#OTHER POSSIBLE GAMES: Checkers

#changes color and player for human playable version
def opposite(color, player, b):
    if color == b.red:
        color = b.blue
    else:
        color = b.red
    if player == "One":
        player = "Two"
    else:
        player = "One"
    return [color, player]

#human playable version of connect 4
def humans():
    #default board
    b = board(6, 7)

    #Settings
    start = raw_input("Start Color (r, b): ")

    color = b.blank
    if start[0] == 'r':
        color = b.red
    else:
        color = b.blue

    player = "One"
    b.printBoard()

    while not b.gameOver:
        valid = False
        while not valid:
            print ("")
            i = raw_input("Player " + player + " column: ")
            print ""
            #valid input
            try:
                valid = b.updateBoard(int(i), color)
            except:
                valid = False

            if not valid:
                print "Bad Move"
                print ""
                b.printBoard()
        b.printBoard()
        b.checkGame()
        nex = opposite(color, player, b)
        color = nex[0]
        player = nex[1]

    print b.winner + " WINS!!"

#changes ai from one to two along with color
def changePlayer(player, one, two, board):
    if player == one:
        return [two, board.blue]
    return [one, board.red]


#finds winner name based on color for ai game
def winner(color, red, blue, board):
    if color == board.red:
        return red + "(red)"
    return blue + "(blue)"

#finds winner name based on color for ai game
def winnerMultiple(color, red, blue, board):
    if color == board.red:
        return red
    return blue

#ai playable version of connect 4, can change ai in player 1 and player 2
def ai():
    #player 1, color red, must have function ai(board)
    one = randobot()
    red = "randobot"

    #player 2, color blue, must have function ai(board)
    two = medium()
    blue = "medium"

    #default board
    b = board(6, 7)

    #variables that change throughout game
    player = one
    color = b.red

    while not b.gameOver:
        b.updateBoard(player.ai(b, color), color)
        b.checkGame()
        update = changePlayer(player, one, two, b)
        player = update[0]
        color = update[1]

    b.printBoard()
    print winner(b.winner, red, blue, b) + " WINS!!"

#ai playable version of connect 4, can change ai in player 1 and player 2, numGames for how many games to be played
def aiMultipleGames(numGames):
    #player 1, color red, must have function ai(board)
    one = randobot()
    red = "medium"

    #player 2, color blue, must have function ai(board)
    two = mediumThreat()
    blue = "threat"

    count = 0
    oneCount = 0
    twoCount = 0

    while count < numGames:
        #default board
        b = board(6, 7)

        #variables that change throughout game
        player = one
        color = b.red

        while not b.gameOver:
            b.updateBoard(player.ai(b, color), color)
            b.checkGame()
            update = changePlayer(player, one, two, b)
            player = update[0]
            color = update[1]

        win = winnerMultiple(b.winner, red, blue, b)
        if win == red:
            oneCount += 1
        elif win == blue:
            twoCount += 1
        count += 1

    #print total wins by each
    print "Total Wins:"
    print red + ": " + str(oneCount)
    print blue + ": " + str(twoCount)


#average win percentage by one bot against all others
def gauntlet(t, numGames):
    l = []

    #add bots here -----------------------------------
    r = randobot()
    if t != "randobot":
        l.append(r)
    e = easy()
    if t != "easy":
        l.append(e)
    m = medium()
    if t != "medium":
        l.append(m)
    mp = mediumPrime()
    if t != "mediumPrime":
        l.append(mp)
    mt = mediumThreat()
    if t != "mediumThreat":
        l.append(mt)

    totalWins = 0
    totalLosses = 0

    for i in l:
        #player 1, color red, must have function ai(board)
        one = i

        #change this based off type of gauntlet--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        two = randobot()

        count = 0

        while count < numGames:
            #default board
            b = board(6, 7)

            #variables that change throughout game
            player = one
            color = b.red

            while not b.gameOver:
                b.updateBoard(player.ai(b, color), color)
                b.checkGame()
                update = changePlayer(player, one, two, b)
                player = update[0]
                color = update[1]

            if b.winner == b.red:
                totalLosses += 1
            elif b.winner == b.blue:
                totalWins += 1
            count += 1

    for i in l:
        #player 1, color red, must have function ai(board)
        two = i

        #change this based off type of gauntlet------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        one = randobot()

        count = 0

        while count < numGames:
            #default board
            b = board(6, 7)

            #variables that change throughout game
            player = one
            color = b.red

            while not b.gameOver:
                b.updateBoard(player.ai(b, color), color)
                b.checkGame()
                update = changePlayer(player, one, two, b)
                player = update[0]
                color = update[1]

            if b.winner == b.red:
                totalWins += 1
            elif b.winner == b.blue:
                totalLosses += 1
            count += 1

    print "Gauntlet total for " + t + ": " + str(round(float(float(totalWins) / float(totalWins + totalLosses)), 4) * 100) + "% win percentage"

#main
#aiMultipleGames(1000)
#ai()
gauntlet("randobot", 1000)

