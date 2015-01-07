import random

def aveage(ar):
    Sum = 0
    under0 = 0
    for i in ar:
        Sum += i
        if i < 0:
            under0 += 1
    ave = Sum/len(ar)
    return ave, under0

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif 0 < roll <= 50:
        return False
    elif 50 < roll < 100:
        return True

def simple_better(funds, wage, numOfWages, deviation):
    value = funds
    ndev = deviation*2
    pdev = deviation
    
    for i in range(numOfWages):
        if rollDice():
            value += wage
            wage += pdev
        else:
            value -= wage
            if ndev > wage:
                wage -= ndev

    #print "Funds: ", value
    return value, wage

y = 0
while y < 10:
    y += 1
    x = 0
    values = []
    wages = []
    while x < 1000:
        x += 1
        value, wage = simple_better(10000,100,1000,1000)
        values.append(value)
        wages.append(wage)
    
    ave, under0 = aveage(values)
    avewage, u = aveage(wages)
    print "Average: ", ave, "Under 0: ", under0, "EndWage: ", avewage
