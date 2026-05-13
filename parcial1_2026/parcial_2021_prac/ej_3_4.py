"""
ACT 3
Aplicar busqueda ceros a  p(x): x**3+x-5
con x0=10.0 y x1=-10.0 para 15 iteraciones y tolerancia 1e-6
"""

from ej_1_2 import * # importo todo el archivo
def mi_funcion(x):
    return horn([1, 0, 1, -5], x), horn([3, 0, 1], x)     
hx_best, hf_best = busqueda_ceros(mi_funcion, 10.0, -10.0, 1e-6, 15)

"""
LINEA 8 
en el primer hor pongo los coeficientes de mi polinomio de 
forma decreciente segun las potencias y en el segundo repito el mismo 
proceso pero con la derivada

ACT 4
Graficar p(x) en el intervalo [-2, 4] junto con los ptos
visitados por el metodo que consiga la mejor solucion
"""
import matplotlib.pyplot as plt
a = -2
b = 4
h = (b-a)/99
x = [a + i*h for i in range(100)]
fx = [mi_funcion(i)[0] for i in x]
plt.xlim([-2, 4]) # determino los limites de mi grafico en x
plt.ylim([-20, 80]) # determino los limites de mi grafico en y
plt.plot(x, fx, hx_best, hf_best, "o")
plt.title("mi funcion y el metodo de Newton")
plt.legend(["mi funcion", "iteraciones de Newton"])
plt.show()