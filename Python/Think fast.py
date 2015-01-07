import random

def randchar():
    #Generates a random Char 50% Vowel, 50% Nonvowel
    CharN = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
    CharV = ["A","E","I","O","U"]
    typeof = random.randint(0,1)
    if typeof == 0:
        pos = random.randint(0,len(CharN)-1)
        return CharN[pos]
    else:
        pos = random.randint(0,len(CharV)-1)
        return CharV[pos]

def testChar(c):
    #Returnes True if 'c' is a vowel
    if c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True
    else:
        return False

def interface(a,b,c,d,true):
    #Prints the interface of two cards
    #Each casd has teo slots "a,b" and "c,d"
    #If the previous question is wrong 'true' is set to False
    #A hint will be displayed to the player which card is which
    #Else 'true' is set to True and a normal card shows
    for i in range(1,50):
        print (" ")
    if true:
        print("|-----|")
        print("|",a,b,"|")
        print("|-----|")
        print("|",c,d,"|")
        print("|-----|")
    else:
        print("|-----|")
        print("|",a,b,"|"," <--- Is it Even?")
        print("|-----|")
        print("|",c,d,"|"," <--- Is it a Vowel?")
        print("|-----|")

def newquestion(true):
    #Generates a new question
    #Makes a random number from 1 - 9 and a Random Character
    #Puts them in a random order: 2B, 6C, F9, 1A ....
    #Sets the card they will apear in (0 = top, 1 = bottom)
    #If the position is in the top card it sets 'ans' to True if it is Even
    #If the position is in the bottom card it sets 'ans' to True if it is a Vowel
    #Last it calls 'interface' with the variables and passes on the argument 'true'
    num = random.randint(1,9)
    let = randchar()
    pos = random.randint(0,1)
    order = random.randint(0,1)
    if order == 0:
        first = num
        sec = let
    else:
        first = let
        sec = num
    if pos == 0:
        a = first
        b = sec
        c = " "
        d = " "
        if num%2 == 0:
            ans = True
        else:
            ans = False
    else:
        a = " "
        b = " "
        c = first
        d = sec
        if testChar(let):
            ans = True
        else:
            ans = False

    interface(a,b,c,d,true)

test = True
while test: 
    newquestion(True)
    input(" ")
