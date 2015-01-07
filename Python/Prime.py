import math

def isPrime(num):
    # Returns True if 'num' is Prime
    # Returns False if 'num' is not Prime
    prime = True
    up = int(math.sqrt(num))+2
    for x in range(2,up):
        if num%x == 0:
            prime = False
            break
    return prime

def prime_Numbers(low,up,returnTrue):
    # Prints out number between 'low' and 'up' including
    # If 'returnTrue' equals True returns Array of the numbers
    if returnTrue:
        arrayRet = []
        for x in range(low,up+1):
            if isPrime(x):
                arrayRet.append(x)
        return arrayRet
    else:
        for x in range(low,up+1):
            if isPrime(x):
                print (x)
        

def nextPrime(num):
    # Returns next prime after 'num'
    count = num
    if count%2 == 0:
        count += 1
    while True:
        if isPrime(count):
            return count
        else:
            count += 2
            
def primeFactorising(num):
    factors = []
    check = 1
    count = 2
    maxim = num
    if isPrime(num):
        return False
    while count <= maxim:
        flag = True
        while flag:
            if num%count == 0:
                num = num/count
                factors.append(count)
            else:
                flag = False
                count += 1
    return factors


print (primeFactorising(int(input("Num: "))))
input()

