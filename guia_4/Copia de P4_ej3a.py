""" Obtener los datos almacenados en los archivos datos3a.dat y datos3b.dat para realizar
el ajuste de los siguientes modelos, es decir, determinar los coeficientes de cada modelo:
(a) y(x) = C*x**A
AYUDA
Transformar en cada caso la expresión dada a un modelo lineal, y obtener una recta que
mejor ajusta los datos (transformados) en el sentido de m´ınimos cuadrados.
"""
import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("/home/visitante/Documentos/vj/guia_4/datos3a.dat")
x = datos[0]
y = datos[1]

x_ = np.log(x)
y_ = np.log(y)

coef = np.polyfit(x_, y_, 1) # porque es de grado uno (lineal)

A = coef[0] # termino lineal
C = np.exp(coef[1]) # termino indeprendiente
print("El valor de A es: ", A)
print("El valor de C es: ", C)

# Graficar
plt.plot(x,y,"o", color = "red", label="valores de los datos")
x_plot = np.linspace(1,5,10) # pido x para graficar
y_plot = C*x_plot**A
plt.plot(x_plot, y_plot)
plt.legend()
plt.title("Act 3-(a)")
plt.grid(True, linestyle='--', color='gray')
plt.show()

