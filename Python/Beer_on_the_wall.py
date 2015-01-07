import time
def beer(number,time):
    p = "s"
    for t in range(number,0,-1):
        print (t, "bottle"+p,"of beer on the wall.\n",t, "bottle"+p,"of beer!\n You take one down and pass it around")
        if t == 1:
            print ("No more bottles of beer on the wall!")
            return
        else:
            if time:
                time.sleep(3)
            t -= 1
            if t == 1:
                p = ""
            print (t, "bottle"+p,"of beer on the wall.")
            print ("")

beer(100,False)

input()
