# Ashvin Pidaparti pidap008

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I furthur certify that this program represents my own work. None of it was
# obtained from any source other than material presented as part of the
# course.

import random
import turtle

def tile_maker(x,y,color):          #COMPLETE
    t = turtle.Turtle()             #takes turtle coordinates and creates stamp on board
    t.ht()                          # takes tile turtle coordinates, goes to them and creates a tile at that location
    t.up()
    t.speed(0)
    t.goto(x,y)
    t.color("black", color)
    t.shape("circle")
    t.turtlesize(1.7)
    t.stamp()
    t.up()

def CoordinateStringtoList(CoordinateString):       #COMPLETE
    coordinatelist = [int(CoordinateString[0]),int(CoordinateString[2])]   #converts board coordinates to a list
    return coordinatelist

def CoordinateConverter(row,column):        #COMPLETE
    return [-175 + (column * 50), 175 - (row * 50)]        #takes row and column, returns turtle coordinates for stamping

def boardInfo():            #COMPLETE    #creates initial board info matrix
    board = [["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","white","black","None","None","None"],
    ["None","None","None","black","white","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"]]
    return board

def boardUpdate(board):         #COMPLETE   #updates board at any point
    t = turtle.Turtle()
    t.ht()
    t.up()
    t.speed(0)
    coordinates = []
    for row in range(8):    #iterates through board
        for space in range(8):
            coordinates = CoordinateConverter(row,space)
            if board[row][space] == "white":
                tile_maker(coordinates[0],coordinates[1],"white")   #stamps tile
            elif board[row][space] == "black":
                tile_maker(coordinates[0],coordinates[1],"black")

def createBoard():          #COMPLETE       #creates initial board in turtle graphics
    t = turtle.Turtle()
    t.ht()
    t.speed(0)
    t.color("black","green")
    t.up()
    t.goto(-200, 200)
    t.pd()
    t.begin_fill()
    for i in range(4):  #draws outline
        t.seth(360 - (90 * i))
        t.fd(400)
    t.end_fill()
    t.end_fill()
    t.goto(-200,100)
    t.seth(0)
    for i in range(10):   #creates rows
        t.pd()
        t.fd(400)
        t.up()
        t.goto(-200, 200 - (i * 50))
    t.seth(90)
    t.up()
    t.fd(50)
    for i in range(10):     # creates columns
        t.pd()
        t.fd(400)
        t.up()
        t.goto(-200 + (i * 50), -200)
    for i in range(8):      # writes numbers on left side
        t.up()
        t.goto(-215, 170 - (i * 50))
        t.write(i,font = ("ComicSansMS",11,"bold"))
    for i in range(8):      # writes numbers on right side
        t.up()
        t.goto(-170 + (i * 50),205)
        t.write(i,font = ("ComicSansMS",11,"bold"))
    boardUpdate(boardInfo())



def resetBoard():           #resets board, if user wants to play again, or for convenience in testing
    turtle.clearscreen()
    createBoard()

def CheckSurroundingTiles(board,row,col,color):     #COMPLETE
    if color == "black":
        oppositeColor = "white"
    else:
        oppositeColor = "black"
    colCheckList = [-1,0,1]             # checks surrounding tiles
    rowCheckList = [-1,0,1]
    if row == 7:                    #lines 110 to 116 modify iteration list if in corner or by wall
        rowCheckList = [-1,0]       #if the selected tile is next to a wall or corner, the program should
    if row == 0:                    #only check the tiles that are within the board
        rowCheckList = [0,1]
    if col == 7:
        colCheckList = [-1,0]
    if col == 0:
        colCheckList = [0,1]
    for ycor in rowCheckList:       #iterate through row
        for xcor in colCheckList:   #iterate through columns
            if board[row + ycor][col + xcor] == oppositeColor:
                return True
    for xcor in colCheckList:
        if board[row][col + xcor] == oppositeColor:
            return True

def tileFlip(board,row,col,color):      #outputs list of tiles to flip in row,column form
    flipList = []
    col_inc = col       #column to check if matches tile color
    row_inc = row       # row to check if matches tile color
    while col_inc > 0:             # adds to flip list left of tile
        col_inc -= 1
        if board[row][col_inc] == "None":   #stops loop if empty
            col_inc = 0
        elif board[row][col_inc] == color:
            for i in range(1,col - col_inc):      #needs to be -1 because needs to interate through one less than difference
                if [[row,col_inc + i]] not in flipList:
                    flipList += [[row,col_inc + i]]
            col_inc = 0
    col_inc = col
    while col_inc < 7:        # adds to flip list right of tile
        col_inc += 1
        if board[row][col_inc] == "None":  #stops loop if space is empty
            col_inc = 7
        elif board[row][col_inc] == color:
            for i in range(1,col_inc - col):      #needs to be -1 because needs to interate through one less than difference
                if [[row,col_inc - i]] not in flipList:
                    flipList += [[row,col_inc - i]]
            col_inc = 7
    col_inc = col
    while row_inc > 0:        # adds to flip list up of tile
        row_inc -= 1
        if board[row_inc][col] == "None":   #stops loop if space is empty
            row_inc = -1
        elif board[row_inc][col] == color:
            for i in range(1,row - row_inc):      #needs to be -1 because needs to interate through one less than difference
                if [[row_inc + i,col]] not in flipList:
                    flipList += [[row_inc + i,col]]
            row_inc = 0
    row_inc = row
    while row_inc < 7:             # adds to flip list down of tile
        row_inc += 1
        if board[row_inc][col] == "None":
            row_inc = 7
        elif board[row_inc][col] == color:
            for i in range(1,row_inc - row):
                flipList += [[row_inc - i,col]]
            row_inc = 7
    row_inc = row
    while col_inc > 0 and row_inc > 0:      # adds to flip list left up of tile
        col_inc -= 1
        row_inc -= 1
        if board[row_inc][col_inc] == "None":   #stops loop if space is empty
            col_inc = -1                        # don't need to stop for row_inc because col_inc will stop
        elif board[row_inc][col_inc] == color:
            for i in range(1,col - col_inc):
                if [[row_inc + i,col_inc + i]] not in flipList:
                    flipList += [[row_inc + i,col_inc + i]]
            col_inc = -1
    col_inc = col
    row_inc = row
    while col_inc < 7 and row_inc < 7:        # adds to flip list right down of tile
        col_inc += 1
        row_inc += 1
        if board[row_inc][col_inc] == "None":
            col_inc = 7
        elif board[row_inc][col_inc] == color:
            for i in range(1,col_inc - col):
                if [[row_inc - i,col_inc - i]] not in flipList:
                    flipList += [[row_inc - i,col_inc - i]]
            col_inc = 7
    col_inc = col
    row_inc = row
    while row_inc > 0 and col_inc < 7:      #adds to flip list right up of tile
        col_inc += 1
        row_inc -= 1
        if board[row_inc][col_inc] == "None":
            row_inc = 0
        elif board[row_inc][col_inc] == color:
            for i in range(1,row - row_inc):
                if [row_inc + i,col_inc - i] not in flipList:
                    flipList += [[row_inc + i,col_inc - i]]
            row_inc = 0
    row_inc = row
    col_inc = col
    while row_inc < 7 and col_inc > 0:      #adds left down
        col_inc -= 1
        row_inc += 1
        if board[row_inc][col_inc] == "None":
            row_inc = 7
        elif board[row_inc][col_inc] == color:
            for i in range(1,col - col_inc):
                flipList += [[row_inc - i, col_inc + i]]
            row_inc = 7
    return flipList

def isValidMove(board,row,col,color):           #COMPLETE
    CheckCount = 0
    if row <=7 and row >= 0 and col >= 0 and col <= 7:          #checks if on board
        CheckCount += 1
    if CheckSurroundingTiles(board,row,col,color) == True:      #Checks for surrounding tiles
        CheckCount += 1
    if len(tileFlip(board,row,col,color)) > 0:     #checks if at least one tile flipped
        CheckCount += 1
    if board[row][col] == "None":   # checks if space is empty
        CheckCount += 1
    if CheckCount == 4:     #checks if all of the above are met
        return True
    else:
        return False

def getValidMoves(board,color):         #COMPLETE
    ValidMoves = []
    for row in range(8):
        for space in range(8):
            if isValidMove(board,row,space,color) == True:
                ValidMoves.append((row,space))
    return ValidMoves

def playerMove(board):
    t = turtle.Turtle()
    t.ht()
    t.up()
    t.speed(0)
    boardChange = [["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"]]
    ValidMoves = getValidMoves(board,"black")       #finds valid moves, if none, computer plays
    if len(ValidMoves) == 0:
        return False
    coordinates = turtle.textinput("","enter row,col")
    while len(coordinates) != 3 or coordinates[0] not in "01234567" or coordinates[2] not in "01234567":
        t.color("black")
        t.goto(-150,-250)
        t.write("That is an invalid move. Please select another.",font = ("ComicSansMS",14,"bold"))
        coordinates = turtle.textinput("","enter row,col")
        if coordinates == "":
            return False
    coordinatelist = CoordinateStringtoList(coordinates)        #converts coordinate string to list
    if isValidMove(board,coordinatelist[0],coordinatelist[1],"black") == True:
        t.color("white")
        t.goto(-150,-230)
        t.begin_fill()
        t.seth(0)
        for i in range(2):
            t.fd(300)
            t.right(90)
            t.fd(40)
            t.right(90)
        t.end_fill()
        board[coordinatelist[0]][coordinatelist[1]] = "black"
        boardChange[coordinatelist[0]][coordinatelist[1]] = "black"
        boardUpdate(boardChange)     #board should be updated with played tile before flipped tiles just for the chronology of the move
        for i in tileFlip(board,coordinatelist[0],coordinatelist[1],"black"):
            board[i[0]][i[1]] = "black"        #modifies board matrix to match tiles to be flipped
            boardChange[i[0]][i[1]] = "black"
            boardUpdate(boardChange)
    else:
        t.color("black")
        t.goto(-150,-250)
        t.write("That is an invalid move. Please select another.",font = ("ComicSansMS",14,"bold"))
        playerMove(board)
    if coordinates != "":
        return True

def selectNextPlay(board):
    boardChange = [["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"],
    ["None","None","None","None","None","None","None","None"]]
    ValidMoves = getValidMoves(board,"white")
    if len(ValidMoves) != 0:
        move = ValidMoves[random.randint(0,len(ValidMoves) - 1)]    #picks random move from valid moves
        board[move[0]][move[1]] = "white"
        boardChange[move[0]][move[1]] = "white"
        boardUpdate(boardChange)      #needs to update before flipping tiles for chronology of move
        for i in tileFlip(board,move[0],move[1],"white"):
            board[i[0]][i[1]] = "white"
            boardChange[i[0]][i[1]] = "white"
    else:
        return False
    boardUpdate(boardChange)
    return True

def tileCounter(board,color):       #COMPLETE
    count = 0                       #returns number of tiles of specific color
    for row in board:
        for space in row:
            if space == color:
                count += 1
    return count

def main():         #COMPLETE
    board = boardInfo()
    resetBoard()
    player_move = playerMove(board)
    computer_move = True
    while player_move == True and computer_move == True:
        computer_move = selectNextPlay(board)
        if computer_move == True:
            player_move = playerMove(board)
    computerScore = tileCounter(board,"white")
    playerScore = tileCounter(board,"black")
    turtle.Turtle()
    turtle.ht()
    turtle.up()
    turtle.goto(-150,-250)
    if player_move == False:
        if len(getValidMoves(board,"black")) == 0 and len(getValidMoves(board,"white")) != 0:
            turtle.write("You have no moves remaining",font = ("ComicSansMS",14,"bold"))
        elif len(getValidMoves(board,"black")) == 0 and len(getValidMoves(board,"white")) == 0:
            turtle.write("The board is full!",font = ("ComicSansMS",14,"bold"))
        else:
            turtle.write("You have terminated the game.",font = ("ComicSansMS",14,"bold"))
        turtle.goto(-150,-275)
    if computer_move == False:
        turtle.write("The computer has no moves.",font = ("ComicSansMS",14,"bold"))
        turtle.goto(-150,-275)
    if playerScore > computerScore:
        turtle.write("Congratulations! You have won! The score is " + str(playerScore) + " to " + str(computerScore) + ".",font = ("ComicSansMS",14,"bold"))
    elif computerScore > playerScore:
        turtle.write("The computer has beaten you! The score is " + str(playerScore) + " to " + str(computerScore) + ".",font = ("ComicSansMS",14,"bold"))
    else:
        turtle.write("Tie game!",font = ("ComicSansMS",14,"bold"))

if __name__ == '__main__':
    main()
