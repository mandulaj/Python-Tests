import random, time
next = True
table = int(input("Set the max time-table: "))
resultstime = []
right = 0
wrong = 0
total = 0

def wait():
    #Waits 3 seconds
    for i in range(3,0,-1):
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
    return round((right/total)*100)
    

def avetime(array):
    total = 0
    for i in array:
        total += i
    return round(total/len(array),2)
        

while next:
    question = [generatenum(table),generatenum(table)]
    question.append(question[0]*question[1])
    wait()
    start = time.clock()
    userAns = int(input("What is "+str(question[0])+" x "+str(question[1])+"? "))
    if userAns == question[2]:
        end = time.clock()
        right += 1
        total += 1
        resultstime.append(caltime(start,end))
        print("Yes,",question[0],"x",question[1],"=",question[2])
        print("It took you",resultstime[len(resultstime)-1],"seconds.")
    else:
        end = time.clock()
        wrong += 1
        total += 1
        resultstime.append(caltime(start,end))
        print("No,",question[0],"x",question[1],"=",question[2])
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
    



