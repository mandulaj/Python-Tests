print "A programm for converting Faranheits to Celsius!"
print 

def convert():
    typeT = raw_input("Type c to convert from Celsius to Faranheit or f to convert from Faranheit to Celsius: ")
    if typeT == "c":
        CTemp = int(raw_input("Type your Temperature in Celsius! "))
        FTemp = (CTemp/(5.0/9))+32
        print
        print CTemp,"°C is", FTemp, "°F!"
    elif typeT == "f":
        FTemp = int(raw_input("Type your Temperature in Faranheit! "))
        CTemp = 5.0/9*(FTemp-32)
        print
        print FTemp,"°F is", CTemp, "°C!"
    else:
        print
        print "Sorry type either c or f!"

again = True
while again:
    convert()
    next = raw_input("Do you want to convert again? Y/N: ")
    print
    if next == "N":
        again = False
