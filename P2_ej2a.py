#inciso A
import math 
def fun(x):
    y = math.tan(x)-2*x
    return y
#error<10 a la menos 5, menos de 100 iteraciones
# I = [a,b]
from P2_ej1 import rbisec
hx, hf = rbisec(fun, [0.8,1.4], 1e-5, 100)
n = len(hx)
#pedimos la longitud del intervalo, es indistinto si pido hx o hf
print(n)

""" 
podemos llamar de dos formas, otra opcion es: 
import P2_ej1
hx , hf =P2_ej1.rbisec()
Cuando corremos el programa aparecen 2 corchetes, el primero es referido a los c, ie la mitad del intervalo. Y loss segundos son los valores de f en esos c.
"""

