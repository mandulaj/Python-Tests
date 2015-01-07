
class Field(object):
    
    def createField(self):
        f = []
        for i in range(3):
            f.append([])
            for j in range(3):
                f[i].append(" ")
        return f

    def __init__(self):
        self.field = self.createField()

    def printField(self):
        print ("  A B C")
        it = 1
        for i in self.field:
            print (it ," ".join(i))
            it += 1

    def sTon(self,s):
        s = s.upper()
        if s == "A":
            return 0
        elif s == "B":
            return 1
        elif s == "C":
            return 2
        else:
            return 3
    
    def setC(self,n,s,c):
        s = self.sTon(s)
        n -= 1
        if s > 2 or n > 2 or n < 0 :
            return False
        if self.field[n][s] == " ":
            self.field[n][s] = c
            return True
        else:
            return False

    def parse(self,s):
        if len(s) != 2:
            return False
        try:
            i = int(s[0])
            s = s[1]
        except ValueError:
            try:
                i = int(s[1])
                s = s[0]
            except ValueError:
                return False
        return i,s

    def checkW(self):
        f = self.field
        char = ["O","X"]
        for n in char:
            if (f[0][0] == n and f[0][1] == n and f[0][2] == n) or (f[1][0] == n and f[1][1] == n and f[1][2] == n) or (f[2][0] == n and f[2][1] == n and f[2][2] == n) or (f[0][0] == n and f[1][0] == n and f[2][0] == n) or (f[0][1] == n and f[1][1] == n and f[2][1] == n) or(f[0][2] == n and f[1][2] == n and f[2][2] == n) or (f[0][0] == n and f[1][1] == n and f[2][2] == n) or (f[0][2] == n and f[1][1] == n and f[2][0] == n):
                return n
        return False
        
            

f = Field()
turn = "X"
while True:
    print(5*"\n")
    f.printField()
    print ()
    inp = input("Give me some coords "+turn+": ")
    inp = f.parse(inp)
    if not inp:
        print (2*"\n")
        print("Someting sencible pleace")
        continue
    n = f.setC(inp[0],inp[1],turn)
    if not n:
        print (2*"\n")
        print ("Come on!")
        continue
    ch = f.checkW()
    if ch:
        break
    
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    

print ()    
f.printField()
print ("the winner is",ch)
f.setC(1,"c","0")
            
