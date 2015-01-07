import random

def genseq(length=5):
    seq = ""
    for i in range(0,length):
        seq += str(random.randint(0,9))
    return seq

