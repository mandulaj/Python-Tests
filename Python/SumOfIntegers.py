def add(dow,up):
    a = range(dow,up+1)
    total = 0
    for i in a:
        now = str(i)
        for k in range(0,len(now)):
            total += int(now[k])
    return total

test = True

while test:
    first = int(input("First: "))
    sec = int(input("Second: "))
    print (" ")
    print (add(first,sec))
    print (" ")

    ask = input("Again? y/n ")
    if ask == "n":
        subtest = flas
        test = False
    
            
    
