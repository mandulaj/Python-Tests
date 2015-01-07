run = True
length = 100
loca = 50
state = "a"

def stateA(loc):
 
    if tape[loc] == 0:
        tape[loc] = 1
        global loca
        loca += 1
        global state
        state = "b"
    else:
        tape[loc] = 0
        
        loca -= 1
        
        state = "c"
        
def stateB(loc):

    if tape[loc] == 0:
        tape[loc] = 1
        global loca
        loca -= 1
        global state
        state = "a"
    else:
        tape[loc] = 1
        
        loca += 1
        
        state = "b"
        
def stateC(loc):

    if tape[loc] == 0:
        tape[loc] = 1
        global loca
        loca -= 1
        global state
        state = "b"
    else:
        tape[loc] = 1
        
        loca += 1
        
        state = "stop"

tape = []

for i in range(length):
    tape.append(0)

while run:
    
    if state == "a":
        stateA(loca)
    elif state == "b":
        stateB(loca)
    elif state == "c":
        stateC(loca)
    else:
        break
    print (loca,state)

print (tape)
        
