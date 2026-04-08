# act 7
""""pasos importar math, definir la funcion, 
calcular las raice con un metodo, importar numpy y graficar. 
Hacer de  vuelta para cada metodo """
import math
#funcion f(y,x)=y-e**{-(1-x*y)**2}
def f(y,x):
    return y-math.exp(-1(1-x*y)**2)
#derivada respecto al eje y
def df(y,x):
    return 1-2*x*(1-x*y)*math.exp(-(1-x*y)**2)

#Metodo Newton
from P2_ej3 import rnewton
