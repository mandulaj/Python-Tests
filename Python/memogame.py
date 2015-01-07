import random

def makeBoard(size):
    #Creates a size*size board of "O" in a 2 Dimensional list
    board = []
    for i in range(0,size):
        board.append([])
        for k in range(0,size):
            board[i].append("O")
    return board

def setRandom(board,num):
    #Changes 'num' of "O" in array board to "X"
    for i in range(0,num):
        ag = True
        while ag:
            xran = random.randint(0,len(board[0])-1)
            yran = random.randint(0,len(board[0])-1)
            print (xran,yran)
            if (board[xran][yran] == "O"):
                board[xran][yran] = "X"
                ag = False

#def combin(num):
 #   for i in range()

def printBoard(board):
    #Prints the board in a nice way
    for k in range(0,len(board)):
        print (" ".join(board[k]) )


b = makeBoard(5)
printBoard(b)
setRandom(b,26)
printBoard(b)
