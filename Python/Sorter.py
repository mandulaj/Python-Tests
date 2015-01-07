stack1 = [3,2,1]
stack2 = []
stack3 = []

larg = stack1[0]
def move(origin,dest):
    value = origin[len(origin)-1]
    del origin[len(origin)-1:len(origin)]
    dest.append(value)

def topval(stack):
    if len(stack)>0:
        last = stack[len(stack)-1]
        return last
    else:
        return larg+1

if topval(stack1)

print ("stack1=",stack1,"stack2=",stack2,"stack3=",stack3)
print(topval(stack1))
print(topval(stack2))
move(stack1,stack2)
print ("stack1=",stack1,"stack2=",stack2,"stack3=",stack3)

print(topval(stack1))
print(topval(stack2))
