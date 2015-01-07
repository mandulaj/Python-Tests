import time
n = [8,6,4,6,65,45,4,456,2,56,1,4,456,24,1,9,-5,5,76,345,5,567,4,9,0,1,4,-5,0,-33,-34,345,-1000]
m = n[:]
def sorting(a):
    spot = 0
    while spot < len(a):
        
        if len(a)> spot+1 and a[spot] > a[spot+1]:
            f = a[spot]
            s = a[spot+1]
            a[spot] = s
            a[spot+1] = f
            spot  = 0
        else:
            spot += 1

def ins(lis):
    for i in range(1,len(lis)):
        value = lis[i]
        i = i - 1
        while i >= 0 and (value < lis[i]):
            lis[i+1] = lis[i]
            lis[i] = value
            i = i - 1

print (n) 
t1 = time.clock()
sorting(n)
t2 = time.clock()
print (t2 - t1)
print (n)
print ("\n")
print (m)
t1 = time.clock()
ins(m)
t2 = time.clock()
print (t2 - t1)
print (m)
