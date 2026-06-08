"""Comparación de reglas de integración: Implementar: Punto medio, Trapecio y Simpson
y comparar errores al aproximar: la integral de cero auno de e**(-x)dx
para: N = [4,10,20,40] Construir una tabla."""

import numpy as np

#Definición de la función
def fun(x):
    return np.exp(-x)

a = 0.0
b = 1.0
valor_exacto = 1.0 - np.exp(-1.0)
lista_N = [4, 10, 20, 40]

#Hacemos la aproximacion
def intecomp(fun, a, b, n, regla: str):   
    fa = fun(a)
    fb = fun(b)
    
    if regla == "simpson":
        h = (b - a) / (2 * n)
        sx0 = fa + fb
        sx1 = 0  # suma de terminos impares
        sx2 = 0  # suma de terminos pares
        x = a
        for j in range(1, 2 * n): 
            x = x + h
            if j % 2 == 0:
                sx2 = sx2 + fun(x)  # suma terminos pares
            else:   
                sx1 = sx1 + fun(x)  # suma terminos impares
        sx = (sx0 + 2 * sx2 + 4 * sx1) * (h / 3) 
        return sx
        
    elif regla == "trapecio":
        h = (b - a) / n
        sx0 = fa + fb
        sx1 = 0
        x = a
        for j in range(1, n):
            x = x + h
            sx1 = sx1 + fun(x)
        sx = (sx0 + 2 * sx1) * (h / 2) 
        return sx
        
    elif regla == "pm":
        h = (b - a) / n
        sx = 0.0
        # Recorremos los n subintervalos calculando su punto medio
        for j in range(n):
            x_medio = a + (j + 0.5) * h
            sx = sx + fun(x_medio)
        return sx * h

#Cálculo de Errores y Construcción de la Tabla
for n in lista_N:
    # Calculamos las aproximaciones usando TU función intecomp
    aprox_pm = intecomp(fun, a, b, n, "pm")
    aprox_tr = intecomp(fun, a, b, n, "trapecio")
    aprox_sm = intecomp(fun, a, b, n, "simpson")
    
    # Calculamos los errores absolutos
    err_pm = abs(valor_exacto - aprox_pm)
    err_tr = abs(valor_exacto - aprox_tr)
    err_sm = abs(valor_exacto - aprox_sm)

print("error con pm =",err_pm)
print("error con trapecio =", err_tr)
print("error con simpson =", err_sm)