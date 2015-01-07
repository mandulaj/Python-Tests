class Test(object):

    test = 2
    def __init__(self,color,speed,typeOfit):
        self.color = color
        self.speed = speed+2
        self.typeOfit = typeOfit

    def printVar(self):
        print (self.color)
        print (self.speed)
        print (self.typeOfit)

test = Test("blue",1,False)
test1= Test("red",2,False)
test.printVar()
test1.printVar()

