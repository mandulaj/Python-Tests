import random

goal = "HELO WORLD"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
chance = 10


def newDNA():
    ret = ""
    for i in range(0,len(goal)):
        ret += abc[random.randint(0,len(abc)-1)]
    return ret

def fitness(dna):
    fit = 0
    for i in range(0,len(dna)):
        if dna[i] == goal[i]:
            fit += 1
    return fit


def mutate(dna):
    new = ""
    for i in range(0,len(dna)):
        if dna[i] == goal[i]:
            new += dna[i]
        else:
            if random.randint(1,chance) == 1:
                new += abc[random.randint(0,len(abc)-1)]
            else:
                new += dna[i]

    return new

def clone(dna):
    ret = []
    for i in range(0,50):
        ret.append(dna)

    return ret

def getFitest(pool):
    ind = 0
    fit = 0
    for i in range(0,len(pool)):
        f = fitness(pool[i])
        if f > fit:
            ind = i
            fit = f
    return pool[ind]

def evolve():
    final = newDNA()
    print (final)
    count = 0
    while fitness(final) < len(goal):
        count += 1
        pool = clone(final)
        for i in range(0,len(pool)):
            pool[i] = mutate(pool[i])
        final = getFitest(pool)
        print (final)
           
    print ("It took:", count)
    return final

t = True
while t:
    goal = input("Goal: ")
    goal = goal.upper()
    chance = int(input("Chance: "))
    evolve()
    if input("Again? ") == "N":
        t = False
