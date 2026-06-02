"""(c)Dada la recta y =(3/4)x −1/2
Generar un conjunto de pares (xi, yi), i = 0, . . . , 19,
en el intervalo [0, 10], con dispersi´on normal en el eje y. Realizar un ajuste lineal
a los datos, obtener los coeficientes y dibujar el ajuste. Investigar los comandos:
linspace, randn, polyval y polyfit (NumPy)."""

import numpy as np
import matplotlib.pyplot as plt

def fun (x):
     y = (3/4)*x-0.5
     return y

x = np.linspace(0,10, 20)
y = fun(x)

error = np.random.randn(len(x))  #Lo generamos artificialmente para poder usar las funciones polyval y polyfit
y_nueva = y + error
coefs = np.polyfit(x, y_nueva, 1) #1 es por el grado de la recta
a1 = coefs[1]
a0 = coefs[0]

x_recta = np.linspace(0, 10, 100)
y_ajuste = np.polyval(coefs, x_recta)

# Graficar
plt.plot(x, y_nueva,"o", label="datos con el error")
plt.plot(x_recta,y_ajuste, "--", label="ajuste")
plt.plot(x, y, label="recta real")
plt.legend()
plt.grid(True, linestyle='--', color='gray')
plt.show()





