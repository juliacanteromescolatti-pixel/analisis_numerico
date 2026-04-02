#inciso B
import math 
def fun_lab2ej2b(x):
    y = (x**2)-3
    return y
#error<10 a la menos 5, menos de 100 iteraciones
# I = [a,b]
from P2_ej1 import rbisec
hx, hf = rbisec(fun_lab2ej2b, [1,2], 1e-5, 100)
n = len(hx)
#pedimos la longitud del intervalo, es indistinto si pido hx o hf
print(n)
"""Como el ejercicio me dice que tome raiz de 3 tomo un intervalo en donde uno de las extremos sea menor a raiz de 3 y el otro sea mayor. en nuestro caso tomamos raiz de uno y de 4"""
