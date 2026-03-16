import math
# OVERFLOW
def test_while(base=2):
    exp = 14500
    while exp < 14502:
        print(base**exp)
        exp = exp + 1
    return base**(exp-1)

def overflow(base=2):
    exp = 1
    while math.isinf(base**exp) == False:
        print(base**exp)
        exp = exp + 1
    return base**(exp-1)

overflow()

#act 3 UNDERFLOW
# def suma_aleatorio(s=2):
#     contador =0
#     while 
