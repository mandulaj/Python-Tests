import random, time
next = True
test1 = True
test2 = True
testingout = True

while test1:
    try:
        table = int(input("Set the max time-table: "))
        test1 = False
    except:
        print ("It has to be a number!")
   
while test2:
    try:
        timerlen = int(input("Set the timer: "))
        test2 = False
    except:
        print ("It has to be a number!")

while testingout:
    typeof = input("Type 'm' for muliplication and division mode, 'a' for addition and substraction or 'b' for both! ")
    if typeof == "a" or typeof == "m" or typeof == "m":
        testingout = False
    else:
        print ("You have to type 'm', 'a' or 'b'!")
        testingout = True
        
resultstime = []
right = 0
wrong = 0
total = 0

def wait(timerlen):
    #Waits 3 seconds
    for i in range(timerlen,0,-1):
        print(i)
        time.sleep(1)       
    
def generatenum(max):
    #Generater a number for the question (between 0 and what the user specified)
    numb = random.randrange(0,max+1)
    return numb

def caltime(start,end):
    #Calculates time taken
    return round(end-start,1)

def result(right,total):
    #calculates the result percentage
    return round((right/total)*100)
    

def avetime(array):
    #calculates the average time taken
    total = 0
    for i in array:
        total += i
    return round(total/len(array),2)

def typeofq(var):
    #makes a random operation acording to what thje mode is
    if var == "m":
        rand = random.randrange(1,3)
        if rand == 1:
            return "*"
        else:
            return "/"
    elif var == "a":
        rand = random.randrange(1,3)
        if rand == 1:
            return "+"
        elif rand == 2:
            return "-"
        else:
            return "+"
    elif var == "b":
        rand = random.randrange(1,5)
        if rand == 1:
            return "+"
        elif rand == 2:
            return "-"
        elif rand == 3:
            return "*"
        elif rand == 4:
            return "/"
        else:
            return "+"

def question_gen(typeof):
    #generates question according to what the mode is (m, a, b) in the form of an array --> (0 = fist 1 = second 2 = answer 3 = sign)
    global question
    question = [generatenum(table),generatenum(table)]
    if typeof == "m":
        sign = typeofq("m")
        if sign == "*":
            question.append(question[0]*question[1])
            question.append("*")
        else:
            fist = question[0]
            sec = question[1]
            if sec == 0:
                sec += 1
            mul = fist*sec
            question = [mul,sec,fist,"/"]
    elif typeof == "a":
        sign = typeofq("a")
        if sign == "+":
            question.append(question[0]+question[1])
            question.append("+")
        else:
            question.append(question[0]-question[1])
            question.append("-")
    elif typeof == "b":
        sign = typeofq("b")
        if sign == "*":
            question.append(question[0]*question[1])
            question.append("*")
        elif sign == "/":
            fist = question[0]
            sec = question[1]
            if sec == 0:
                sec += random.randrange(1,7)
            mul = fist*sec
            question = [mul,sec,fist,"/"]
        elif sign == "+":
            question.append(question[0]+question[1])
            question.append("+")
        elif sign == "-":
            question.append(question[0]-question[1])
            question.append("-")
        

while next:
    wait(timerlen)
    question_gen(typeof)
    start = time.clock()
    try:
        userAns = int(input("What is "+str(question[0])+" "+str(question[3])+" "+str(question[1])+"? "))
    except Exception as ex:
        print ("You have to type something. In this case it was supposed to be",question[2],"!")
        userAns = -1000000000000000000000000000000000000000000000000000000000000000
    if userAns == question[2]:
        end = time.clock()
        right += 1
        total += 1
        resultstime.append(caltime(start,end))
        print("Yes,",question[0],str(question[3]),question[1],"=",question[2])
        print("It took you",resultstime[len(resultstime)-1],"seconds.")
    else:
        end = time.clock()
        wrong += 1
        total += 1
        resultstime.append(caltime(start,end))
        print("No,",question[0],str(question[3]),question[1],"=",question[2])
        print("It took you",resultstime[len(resultstime)-1],"seconds.")
    conti = input("Do you want to continue? y/n ")
    if conti.capitalize() == "N":
        next = False
        print(" ")
        print("In total from",total,"you got",right,"right and",wrong,"wrong")
        print("This is", result(right,total), "% success!")
        print("On average, it took you",avetime(resultstime),"seconds!")
        input()
    else:
        next = True
    

