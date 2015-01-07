"""This module enables the creation of different number bases. To create a base make a object using the Base() constructer.
The parentheses take the base number such as 2 or 16. If the base number is greater than the number of character provided in a list it sets it automatically to the max that is possible.
The parentheses can tale a additional optional argument of costume list of characters.
The object can convert from base 10 to the base of the object or the other way around usig the methodes:
    fromB10(n)
    toB10(s)
respectively.
The method toB10() takes a string as a input and returns a number, fromB10() takes a number and returns a string.
"""




import math

ch = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","]","}","|",":",";","'","<",",",">",".","?","/","\\","\""]


def createbase(b):
    ret = ch[:b]
    return ret

class Base(object):
    
    def __init__(self,base,chare = -1):
        # Initializes the Object: sets self.base to base and the list of characters to the correct list.
        
        self.base = base
        if chare != -1 and len(chare) > base:
            self.char = chare[:base]
        else:
            if base < len(ch):
                self.char = createbase(base)
            else:
                self.base = len(ch)
                self.char = createbase(len(ch))

    def getBase(self):
        # Returns the base
        
        return self.base

    def getChar(self):
        # Returns the list of char
        
        return self.char

    def toChar(self,n,char=[]):
        # Returns a String of the corresponding character to n in base 10 from the list of 'char'
        # 'n' has to be a int
        # 'char' is default the characters in the base that calls the function
        # however it can be overridden by providing a list of chars
        
        if len(char) == 0:
            char = self.getChar()
        try:
            return str(char[n])
        except:
            print ("Error")

    def liToStr(self,li,char):
        # Converts a list 'li' of integers into a number in base of 'char'
        # e.g. [6, 14] = "6E" with standard char provided
        
        ret = ""
        for x in li:
            ret += self.toChar(x,char)
        return ret
        
    def toB10(self,n):
        # Converts a string of base 'self' to base 10
        
        n = str(n)
        ans = 0
        powe = 0
        for x in range(len(n)-1,-1,-1):
            ans += (self.char.index(n[x]))*(self.base**powe)
            powe +=1
        return ans
    
    def fromB10(self,n,bx = None,char=[]):
        # Converts 'n' from base 10 to base bx
        # 'bx' can specify a diffeent base, default is the base of the object
        # 'char' can specify a uniqe list of chars, else it is befault to the base of object
        
        if bx == None:
            bx = self.base
            #print "bx =",bx
        if len(char) == 0:
            char = createbase(bx)
            #print "char=",char
        
        li = []
        while n > 0:
            qu = math.floor(n/bx)
            re = n % bx
            n = qu
            li.append(int(re))
        li.reverse()
        ret = self.liToStr(li,char)
        return ret

    def bYtobX(self,x,y,bx=-1,by=10):
        if bx == -1:
            bx = self.base
        pass
        


base2 = Base(2)
n = base2.fromB10(10)
print (n)

c = 0
for x in ch:
    print (c,x)
    c += 1
