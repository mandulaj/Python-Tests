class Animal(object):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = 2*c

    def add(self,add):
        self.b += add






c = Animal("ahoj",3,6)
b = Animal("AHOJ",2,8)

print (c.b)
c.add(6)
print (c.b)

class Dog(Animal):

    def ADD(self):
        return 4

dog = Dog("Jakub",5,6)

print (dog.a)
