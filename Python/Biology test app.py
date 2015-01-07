import time, random

def newQuestion(level):
    arrayOfnum = []
    for i in range(0,level-1):
        arrayOfnum.append(random.randint(0,9))
    out1 = ' '.join(str(e) for e in arrayOfnum)
    out2 = ''.join(str(e) for e in arrayOfnum)
    print (out1)
    return out2

def break_(wait):
    if wait:
        time.sleep(2)
    for k in range(0,50):
            print(" ")


running = True
level = 3
maxlevel = 0
score = 0
lives = 3
def intro():
    running = True
    print ("Welcome to my short-term memory tester.")
    time.sleep(2)
    print (" ")
    print ("We will start by a practice question.")
    time.sleep(2)
    print (" ")
    print ("Your goal is to remember all the numbers \nand type them later into the command line.")
    time.sleep(2)
    print (" ")
    input("Press Enter to Start")
    print (" ")
    while running:
            quest = newQuestion(3)
            break_(True)
            ans = str(input("Type your Answer Here: "))
            print("")
            if quest == ans:
                running = False
                print ("Yes")
                print (" ")
                print ("Now let's start the experiment!")
                print (" ")
                input("Press Enter to Start")
            else:
                print ("No you should have written",quest,"not",ans,"!")
                input("Press Enter to try again!")
intro()           
running = True
print("Ok let's start:")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Go!")
print(" ")

while running:
    if lives == 0:
        break
    quest = newQuestion(level)
    break_(True)
    ans = str(input("Type your Answer Here: "))
    print("")
    if quest == ans:
        score += level*5+10
        print(" ")
        print("You got it!")
        print(" ")
        time.sleep(1)
        level+=1
        break_(False)
    else:
        lives -= 1
        print(" ")
        print("No it was supposed to be",quest)           
        if level > 3:
              level -= 1
              time.sleep(1)
              break_(False)
            
print("Game Over")
print("Your score: ",score)
input(" ")

