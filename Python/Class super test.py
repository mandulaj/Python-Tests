class Main(object):
    def __init__(self,number):
        self.number = number

    def mainM(self):
        print ("This is the super method" , self.number)

class Sub(Main):

    def mainM(self):
        print ("This is the sub method", self.number)

    def sup(self):
        super(Sub,self).mainM()
        
t = Main(1)
t.mainM()

sub = Sub(2)
sub.mainM()
sub.sup()
