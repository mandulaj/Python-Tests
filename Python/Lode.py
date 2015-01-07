def genGrid(n):
    # Generates a n*n field of "O"
    m = []
    for x in range(0,n):
        a = []
        m.append(a)
        for i in range(0,n):
            a.append("O")
    
    return m

def printGrid(grid):
    # Prints the grid in a neat format (each cell joined by a space)
    for x in grid:
        x = " ".join(x)
        print (x)

def strToInt(integer):
    # Converts a sting base 27 "'space', a, b,..,y, z" into a integer
    # Returns 1 if error
    # e.g. " " = 0, "a" = 1, "a " = 27, "aaa" = 757 ...
    alph = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    try:
        i = integer.upper()
        ans = 0
        powe = 0
        for x in range(len(i)-1,-1,-1):
            ans += (alph.index(i[x]))* 27**powe
            powe +=1
    except:
        return 1
    return ans

def getCoord(x,y,grid):
    # Returns the value of 'grid' at 'x', 'y'
    # y = vertical
    # x = horizontal
    # Returns None if 'x' or 'y' is out of range
    try:
        x = int(x)
        
    except:
        x = strToInt(x)
    try:
        y = int(y)
    except:
        y = strToInt(y)
    x -= 1
    y -= 1
    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid):
        return grid[y][x]
    else:
        return None 
G = [["a","b","c"],["d","e","f"],["g","h","i"]]

printGrid(G)
print (getCoord(2,"b",G))

printGrid(genGrid(10))
