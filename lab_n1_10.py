import random

def sonreciprocos(x,y):
    if x*y==1:
        return True
    else:
        return False


for _ in range(100):
    x = 1 + random.random()
    y = 1 / x
    if not sonreciprocos(x,y):
        print(x)