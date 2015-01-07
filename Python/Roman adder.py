import math

def syntaxe(str):
    return "Syntax Error:",str

def convertToRom(num):
    # Converts num into a roman numeral and returns it as a string
    x = 0
    stri = ""
    arr = []
    num = str(num)
    for i in num[::-1]:
        arr.append((10**x)*int(i))
        x+=1
    pos = 0
    for i in arr[::-1]:
        dig = len(arr)-pos
        if dig > 3:
            stri += "M"*(i/1000)
        else:
            if dig == 2:
                
        pos += 1  
    print stri

convertToRom(999999999)      
       

def convertToNum(str):
    # Converts a string into a array of corresponding numbers
    # Then converts the array into the final number
    str = str.upper()
    char = []
    count = 0
    skip = False
    
    # Assigns a corresponding values for each letter including pi!
    for i in str:
        if not skip:
            if i == "I":
                char.append(1)
            elif i == "V":
                char.append(5)
            elif i == "X":
                char.append(10)
            elif i == "L":
                char.append(50)
            elif i == "C":
                char.append(100)
            elif i == "D":
                char.append(500)
            elif i == "M":
                char.append(1000)
            elif i == "P" and len(str) > count+1 and str[count+1] == "I":
                char.append(2.141592653589793238462643383279502884197169399)
                count+= 1
            else:
                print ("exit")
                ca = "Inproper value "+i
                print (syntaxe(ca))
            	return False
        count += 1

    i = 0     # Initialization
    num = 0
    
    # Loops through the array and adds the numbers together accordingly
    while i < len(char):
        if i+1 < len(char) and char[i] > char[i+1]:
            num += char[i]
            i+=1
        elif i+1 < len(char) and char[i] < char[i+1]:
            num += char[i+1] - char[i]
            i += 2
        else:
            num += char[i]
            i+=1
            
    return num




def whatSign(str):
    # Returns the place where +, -, / or * is located ele returns None
    # Takes a String as input
    sign = str.find("+") # Checks what the sign is
    if sign == -1:
        sign = str.find("-")
        if sign == -1:
            sign = str.find("*")
            if sign == -1:
                sign = str.find("/")
                if sign == -1:
                    print (syntaxe("Bad sign"))
                    return None
    return sign

def inputPharser(string):
    # Main method removes any spaces and determines the operation sign
    # Calls convertToNum() to convert each side of the equation into a number
    # Carries out the corresponding function operation with the two numbers
    # Returns the answer

    if string == "exit":
        LOOP = False
        return


    string = string.replace(" ","") # Removes spaces from the expression
    
    sign = 0                   #\
    sign += string.count("+")   #\
    sign += string.count("-") ####> Adds one to the var 'sign' for each operation found
    sign += string.count("/")   #/ 
    sign += string.count("*")  #/
    
    if sign != 1: #If no sign returns converted number
        return convertToNum(string)
    else:
        sign = whatSign(string)
        types = string[sign]
        fir = string[:sign] # sets 'fir' to the left side of the expression
        sec = string[sign+1:] # sets sec to the right part of the expression
        
        if fir.isdigit() == False: # If numeric it converts them to a int
        	fir = convertToNum(fir) # Calls convertToNum to convert each numeral to base 10 number
        else:
        	fir = int(fir)
        	
        if sec.isdigit() == False: 
        	sec = convertToNum(sec) # Calls convertToNum to convert each numeral to base 10 number
        else:
        	sec = int(sec)
        
        if fir == False or sec == False:
            return 0
       
        
        if types == "+":
            ans = fir+sec
        elif types == "-":
            ans = fir-sec
        elif types == "*":
            ans = fir*sec
        elif types == "/":
            fir = float(fir)
            sec = float(sec)
            ans = fir/sec
        else:
            print (syntaxe("Bad Sign"))
            return 0
        
    return ans

def mainLoop():
    LOOP = True
    while LOOP:
        i = raw_input("")
        print (inputPharser(i))

if __name__== "__main__":
    mainLoop()

