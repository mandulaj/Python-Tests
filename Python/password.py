#-*- coding: utf-8 -*- 

import random
def makepassword(length):
    finnal = []
    letter1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    letter2=["A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    symbol1=["!","£","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}",";",":","'","@","#","~",",","<",".",">","/","?",] 
    number1=["1","2","3","4","5","6","7","8","9"]
    for x in range(1,length+1):
        typeofC = random.randint(1,4)
        if typeofC == 1:
            char = random.choice(letter1) 
        elif typeofC == 2:
            char = random.choice(letter2)
        elif typeofC == 3:
            char = random.choice(symbol1)
        else:
            char = str(random.randint(0,9))

        finnal.append(char)

    password = ""
        
    for y in range(0,length):
        password += finnal[y]
        
    return password

test = True
while test:
    print("We are now going to make you a new strong password !")
    lengthofpass = int(input("How long should it be? "))
    print(" ")
    print("Your new password is: ")
    passw = makepassword(lengthofpass)
    print (passw)
    print(" ")

    decision=input("would you like me to write a passord to a textfile Y/N?") 
    if decision=="Y": 
        writing=open("Generated Password.txt","w") 
        writing.write(passw) 

    nextd = input("Again?")
    if nextd == "n":
        test = False

