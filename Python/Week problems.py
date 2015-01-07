import math

def factors(n):
    max,ret = int(math.sqrt(n)),[]
    for i in range(1,max+1):
        if n % i == 0:
            ret.append(i)
            ret.append(int(n/i))
    ret.sort()
    return ret

def sumOfList(*args):
    tot = 1
    for i in args:
        Sum = 0
        if len(i) == 0:
            continue
        Sum = sum(i)
        tot *= Sum
    return tot

def isPalindrome(i):
    i = str(i)
    i = i.replace(" ","")
    c, res = 0, True
    while c<len(i)/2:
        if not i[c] == i[(c+1)*-1]:
            res = False
            break
        c += 1
    return res

def isPalindrome2(i):
    i = i.replace(" ","")
    if i == i[::-1]:
        return True
    else:
        return False

def letterCombinations(s):
    for 

print (isPalindrome2('1221'))
    
