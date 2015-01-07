import time
num = 1

def printNum():
    global num
    time.sleep(1)
    print(num)
    
def prep(cb):
    cb()
    global num
    time.sleep(1)
    num += 1
    
prep(printNum)
