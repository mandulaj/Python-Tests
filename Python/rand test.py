import random

def long(p):
    prob = p
    inte = 0
    while inte != 1:
        prob += 1
        inte = random.randint(0,prob)
    return prob

for n in range(100):
    s = []
    for i in range(1000):
        s.append(long(n))
    print ("Prob value:",n)
    print ("Average:",sum(s)/len(s)) 
    print ("Largest:",max(s),"\n")

input()
