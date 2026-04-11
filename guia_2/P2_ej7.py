# act 7
""""pasos importar math, definir la funcion, 
calcular las raices con un metodo, importar numpy y graficar. 
Hacer de  vuelta para cada metodo """

#FUNCION BASE
import numpy as np

def F(y, x):
    return y - np.exp(-(1 - x*y)**2)

#METODO DE BISECCION
def biseccion(x, a, b, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        m = (a + b) / 2

        if F(a, x) * F(m, x) < 0:
            b = m
        else:
            a = m

        if abs(b - a) < tol:
            return (a + b) / 2

    return (a + b) / 2

#DERIVADA PARA NEWTON
def dF(y, x):
    return 1 + 2*x*(1 - x*y)*np.exp(-(1 - x*y)**2)

#METODO DE NEWTON
def newton(x, y0, tol=1e-6, max_iter=100):
    y = y0

    for _ in range(max_iter):
        y_new = y - F(y, x) / dF(y, x)

        if abs(y_new - y) < tol:
            return y_new

        y = y_new

    return y

#METODO DE PUNTO FIJO
def g(y, x):
    return np.exp(-(1 - x*y)**2)


def punto_fijo(x, y0, tol=1e-6, max_iter=100):
    y = y0

    for _ in range(max_iter):
        y_new = g(y, x)

        if abs(y_new - y) < tol:
            return y_new

        y = y_new

    return y

#LO QUE ME PIDE EL EJERCICIO UNA VEZ QUE YA ESFRIBI LO ANTERIOR
def u_bis(x):
    return biseccion(x, 0, 1)

def u_newton(x):
    return newton(x, 0.5)

def u_pf(x):
    return punto_fijo(x, 0.5)

#PARA GRAFICAR
import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(0, 2, 100)

yb = [u_bis(x) for x in xs]
yn = [u_newton(x) for x in xs]
yp = [u_pf(x) for x in xs]

plt.plot(xs, yb, label="Bisección")
plt.plot(xs, yn, label="Newton")
plt.plot(xs, yp, label="Punto fijo")

plt.legend()
plt.grid()
plt.show()
