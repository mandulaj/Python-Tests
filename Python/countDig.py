def countDig(num):
   tot = 0
   for i in range(0,num+1):
      n = str(i)
      for f in n:
         tot+= int(f)
    return tot
    
print (countDig(1000000))