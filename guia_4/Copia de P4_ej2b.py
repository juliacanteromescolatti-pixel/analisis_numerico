""" 
Para las siguientes funciones generar un conjunto de datos 
(xi, yi), i = 0, . . . , 49 y realizar
un ajuste polinomial de grado n con n = 0, . . . , 5:
(b) g(x) = cos(x), x ∈ [0, 4π].
"""

import numpy as np
import matplotlib.pyplot as plt
 # creamos una lista con los grados
def fun (x):
     y = np.cos(x)
     return y

x = np.linspace(0,4*np.pi, 50)
y = fun(x)
for n in range(6):
    coefs = np.polyfit(x, y, n) # grado 
    y_ajuste = np.polyval(coefs, x)

    error = y - y_ajuste
    y_nueva = y + error

    suma_err = np.sum(error)
    suma_cuad = np.sum(error**2)
    print(n, suma_err)
