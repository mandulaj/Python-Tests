listofchar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
test = ["1","2","3","4"]

def make():
    for i in listofchar:
        for k in listofchar:
            for l in listofchar:
                print (i+k+l)


def arg(num,src):
    if num > 0:
        for x in src:
            return (x + arg(num-1,src))
    else:
        return

#print (arg(4,test))

def req(n):
    if n > 0:
        return n*req(n-1)
print (req(2))
