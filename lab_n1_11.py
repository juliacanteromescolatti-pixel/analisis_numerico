import math
#f(x)=sqrt(x**2 +1)-1
def f(x):
    return math.sqrt(x**2 +1)-1
#g(x):x**2/(sqrt(x**2+1) +1)
def g(x):
    return x**2/(math.sqrt(x**2+1)+1)

#pedimos un numero:
#x=float(input("ingrese un numero"))

#print("f(x)",f(x))
#print("g(x)",g(x))

#bucle para probar varios valores
for i in range(20):
    x=8**-i
    print(f"f(x)={f(x)},g(x)={g(x)},diff:{f(x)-g(x)}")
