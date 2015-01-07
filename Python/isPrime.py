import math

def isPrime(num):
    primet = True
    sq = math.sqrt(num)
    x = 2
    while(x <= sq):
        if num%x == 0:
            primet = False
            break
        x += 1
        
        

    return primet

n = True
while n:
    prime = int(input("Is prime? "))
    print (isPrime(prime))
    x = input("Again? ")
    if x == "n":
        n =False
