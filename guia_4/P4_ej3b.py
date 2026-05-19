""" Obtener los datos almacenados en los archivos datos3a.dat y datos3b.dat para realizar
el ajuste de los siguientes modelos, es decir, determinar los coeficientes de cada modelo:
 (b) y(x) = x/Ax + B
AYUDA
Transformar en cada caso la expresión dada a un modelo lineal, y obtener una recta que
mejor ajusta los datos (transformados) en el sentido de mìnimos cuadrados.
"""
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Leer datos
x, y = np.loadtxt("/home/kmom/analisis_numerico/guia_4/archivos necesarios/datos3b.dat")
# Transformación lineal
y_ = x / y

# Ajuste lineal
coef = np.polyfit(x, y_, 1)

A = coef[0] #termino lineal
B = coef[1] #termono independiente

print("El valor de A es:", A)
print("El valor de B es:", B)


# Graficar
plt.plot(x,y,"o", color = "red", label="valores de los datos")
x_plot = np.linspace(1,5,100) # pido x para graficar
y_plot = x_plot / (A*x_plot + B)
plt.plot(x_plot, y_plot)
plt.legend()
plt.title("Act 3-(b)")
plt.grid(True, linestyle='--', color='gray')
plt.show()

