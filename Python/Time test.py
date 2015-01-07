import time
x = 1
def algorythm(seed):
    timenow1 = time.time()
    timenow = round(timenow1,0)
    timenow = round(timenow/100,0)
    print (timenow)
    n = round(timenow1,0)
    n = abs(n-timenow)
    n = n*10**10
    n = round(n)
    print (n)
    n = (n/seed)*(seed+25)
    n = round(n)
    print (n)
    
while x:
    algorythm(321)
    x = input()
