import math
char2 = ["0","1"]
char10 = ["0","1","2","3","4","5","6","7","8","9"]
base16 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
base = 2

#    2   3  4  5  6  7  8  9  10

#    0   0  0  0  0  0  0  0  0
#    1   1  1  1  1  1  1  1  1
#   10   2  2  2  2  2  2  2  2
#   11  10  3  3  3  3  3  3  3
#  100  11 10  4  4  4  4  4  4
#  101  12 11 10  5  5  5  5  5
#  110  20 12 11 10  6  6  6  6
#  111  21 13 12 11 10  7  7  7
# 1000  22 20 13 12 11 10  8  8
# 1001 100 21 14 13 12 11 10  9
# 1010 101 22 20 14 13 12 11 10
# 1011 102 23 21 15 14 13 12 11
# 1100 110 30 22 20 15 14 13 12
# 1101 111 31 23 21 16 15 14 13
# 1110 112 32 24 22 20 16 15 14
# 1111 120 33 30 23 21 17 16 15

def toChar(n,chars):
    try:
        return str(chars[n])
    except:
        print ("Error")

def liToStr(li,char):
    ret = ""
    for x in li:
        ret += toChar(x,char)
    return ret

def b10toBX(n,bx,char):
    li = []
    while n > 0:
        qu = math.floor(n/bx)
        re = n % bx
        n = qu
        li.append(int(re))
    li.reverse()
    ret = liToStr(li,char)
    return ret

print (b10toBX(112,16,base16))

