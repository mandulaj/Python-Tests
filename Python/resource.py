
def getTime(goal,initial,grow):
    goal -= initial
    time = goal/grow
    print ("To get",goal,"with a growth of",grow,"recources per houre it will take you... \n",time,"hours.")
    return time

while True:
    goal = int(input("How much do you need: "))
    initial = int(input("How much do you have: "))
    grow = int(input("How much do you produce per hour: "))
    t = getTime(goal,initial,grow)
    print("This is",t*60,"minutes.")
    print()
    print()

