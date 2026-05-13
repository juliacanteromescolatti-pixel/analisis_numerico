""" Obtener los datos almacenados en los archivos datos3a.dat y datos3b.dat para realizar
el ajuste de los siguientes modelos, es decir, determinar los coeficientes de cada modelo:
 (b) y(x) = x/Ax + B
AYUDA
Transformar en cada caso la expresión dada a un modelo lineal, y obtener una recta que
mejor ajusta los datos (transformados) en el sentido de m´ınimos cuadrados.
"""
import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("/home/visitante/Documentos/vj/guia_4/datos3a.dat")
x = datos[0]
y = datos[1]

x_ = 1/x
y_ = 1/y

coef = np.polyfit(x_, y_, 1) # porque es de grado uno (lineal)

B = coef[0] # termino lineal
A = np.exp(coef[1]) # termino indeprendiente
print("El valor de A es: ", A)
print("El valor de B es: ", B)

# Graficar
plt.plot(x,y,"o", color = "red", label="valores de los datos")
x_plot = np.linspace(1,5,100) # pido x para graficar
y_plot = (x/A*x_plot+B)
plt.plot(x_plot, y_plot)
plt.legend()
plt.title("Act 3-(b)")
plt.grid(True, linestyle='--', color='gray')
plt.show()

