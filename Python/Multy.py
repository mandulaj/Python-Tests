timeTab = int(input("What time table do you want? "))
low = int(input("Where to start? "))
up = int(input("Where to end? "))
up += 1
print ("Ok here we go!")
for numb in range(low,up):
    print (numb ,"x", timeTab,"=", numb*timeTab)

input()
