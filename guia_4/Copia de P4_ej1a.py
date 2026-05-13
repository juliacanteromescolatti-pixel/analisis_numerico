"""(a) Usando el comando loadtxt de python (np.loadtxt), leer los datos almacenados en el
archivo datos1a.dat ubicado en el aula virtual de la materia. Usar las f´ormulas para
un ajuste lineal por cuadrados m´ınimos para obtener la recta que mejor aproxima
estos datos. Graficar los datos y el ajuste obtenido"""

import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("/home/visitante/Documentos/vj/guia_4/datos1a.dat")
x = datos[0]
y = datos[1]

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xc = np.sum(x**2)
sum_xy = np.sum(x*y)

m = len(x)

a0 = (sum_xc * sum_y - sum_xy * sum_x)/(m*sum_xc-(sum_x)**2)

a1 = (m*sum_xy-sum_x*sum_y)/(m*sum_xc-(sum_x)**2)
	
print(np.sum((y-(a1*x+a0))**2)) #esto es el cuadrado minimo

xi = [0,5]
yi = [a1*xi[0] + a0,a1*xi[1] + a0]
	    			
# Graficar
plt.plot(x, y,"o")
plt.plot(xi,yi)
plt.grid(True, linestyle='--', color='gray')
plt.title("Act 1-(a)")
plt.show()



