
## AI - artificial intelligence
#############################################################
## A program that simulates a artificial intelligence
## May show some talent in mathematics and other stuff
##
##
##
##
##
#############################################################

import sys

PyVersion = sys.version_info[:3] # gets the current python version
RUN = True
Input = "" # global variable used to store the input from command line
Ask = "Hello" # global variable used to store what the computer should ask
Out = "a" # global variable used for output from the computer
NewSession = True   # True if this session is the first (no .ai file found)
Version = "1.0" # Version of this program
NAME = "NaN" # name of AI
FRIENDS = "NaN"
AGE = "NaN"

if (PyVersion[0] >= 3 and PyVersion[1] >= 3):
    # checks if we are using python 3.3 and above
    RUN = True
else:
    RUN = False
    print("You are using a old version of Python! Try using 3.3") # prints a error message if python version is too old


def parseMem(name,mem):
    file = mem.read()
    ans = ""
    pos = file.find(name=":")
    if pos == -1:
        return False
    pos += len(name)+1
    
    while not file[pos] == "\n":
        ans += file[pos]
        pos += 1
    return ans
    
def setUpVariables(mem):
    global NAME, FRIENDS, AGE
    NAME = parseMem("NAME",mem)
    FRIENDS = parseMem("FRIENDS",mem)
    AGE = parseMem("AGE",mem)
    



def setupNEW(mem):
    mem.write("##AI "+Version+"\n")
    mem.write("\n")
    mem.write("NAME:non\n")
    mem.write("FRIENDS:non\n")
    mem.write("AGE:non\n")
    mem.flush()

 
if RUN:
    # Tries to open a AImemo.ai file. If there is a file found in the pwd, NewSession is set to false else a new file is created
    try:
        memo = open("AImemo.ai","r+")
        if memo.readline() == "##AI "+Version:
            NewSession = False
            setUpVariables(memo)
        else:
            setupNEW(memo)
            
    except IOError as err:
        print("Sorry there is a error with my brain. {0}".format(err)) # if there is a error while writing the file program terminates
        RUN = False



def isInStr(search,string,start=False,tolerance=-1):
    Found = False # Used to keep track if string was found
    
    if tolerance < 0:
        tolerance = len(string)# sets the tolerance to 'nothing' by default
    
    search = search.lower() # converts both search string and reference to lowercase
    string = string.lower()
    
    if len(string)<len(search): # returns false if the quary is longer then the string that is searched
        return False
    
    elif (abs(len(search)-len(string))<tolerance) and (string.find(search) >= 0) and not start:
        return True
    elif string.find(search) == 0 and start:
        return True
    else:
        return False # the length of word is out of bounds

    return False


def parse(inStr):
    global Out, Ask, memo
    if isInStr("bye",inStr,True):
        global RUN
        RUN = False
        memo.close()
        Out = "See yea!"
        return
    elif isInStr("name",inStr):
        global NAME 
        Out = NAME
        return
    else:
        Ask = "Hello"
        Out = inStr




while RUN:
    Ask = "AI: " + Ask +"\n"
    Input = input(Ask)
    parse(Input)
    Out = "AI: " + Out
    print(Out)

print(NAME)
print(FRIENDS)
print(AGE)

try:
    end = input()
except:
    print("")
