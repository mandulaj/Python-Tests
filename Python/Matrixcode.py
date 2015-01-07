message = "COME TO DINNER"

key = [[5,2],[3,1]]


def convertToMatrix(msg):
    letters = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nums = []

    if not len(msg)%2 == 0:
        msg += " "
    
    for i in range(len(msg)):
        if not i%2 == 0:
            continue
        matrix = [letters.index(msg[i]),letters.index(msg[i+1])]
        nums.append(matrix)

    return nums

def convertFromMatrix(m):
    letters = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    st = ""

    for i in m:
        for j in i:
            st += letters[int(j)]
    return st

def matrixMultiplicator(mKey,mMsg):
    return[mMsg[0]*mKey[0][0]+mMsg[1]*mKey[1][0] , mMsg[0]*mKey[0][1]+mMsg[1]*mKey[1][1]]

def det(m):
    return m[0][0]*m[1][1]-m[1][0]*m[0][1]

def inverse(m1):
    deter = 1.0/det(m1)

    return [[m1[1][1]*deter,-m1[0][1]*deter],[-m1[1][0]*deter,m1[0][0]*deter]]

def encode(key,msg):
    mat = convertToMatrix(msg)
    res = []
    
    for i in mat:
        res.append(matrixMultiplicator(key,i))
    return res

def decode(key,dec):
    key = inverse(key)
    res = []
    
    for i in dec:
        res.append(matrixMultiplicator(key,i))
    return convertFromMatrix(res)

#print encode(key,message)
#[[111, 40], [129, 48], [125, 50], [95, 37], [82, 32], [47, 16],[100,40]] IVORY PENDANT
# [[47, 16], [42, 15], [67, 24], [100, 40], [85, 33], [48, 17],[63,25],[30,11]] ANCIENT NECKLACE
# [[55, 19], [85, 33], [42, 14], [40, 15], [56, 20], [82, 29]]BONE NEEDLES
print decode(key,[[57, 21], [119, 46], [24, 8], [120, 45], [112, 41]])
