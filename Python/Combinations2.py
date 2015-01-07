def combinations(List,length):
    final = ""
    for i in List:
        print ("con:", length,"It:",i)
        if length > 0:
            final += str(i)+combinations(List,length-1)
            return final
        else:
            return str(i)

print (combinations([1,2,3],3))

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1

print (factorial(10))
