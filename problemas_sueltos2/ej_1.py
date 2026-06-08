#Integración de una función trigonométrica. Calcular: la integral de cero a pi de sen(x) dx
#Con Simpson compuesto. Comparar con el valor exacto.

import numpy as np

# 1. Definición de la función y parámetros
def f(x):
    return np.sin(x)

a = 0.0
b = np.pi
n = 4  # Cantidad de subintervalos (Debe ser PAR)
valor_exacto = 2.0

# 2. Implementación de Simpson Compuesto (Corregida)
def simpson_compuesto(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    res_parcial = 0 
    
    for j in range(len(x)):
        # Si es el primer elemento (j=0) o el último (j=len(x)-1)
        if j == 0 or j == len(x) - 1:
            res_parcial += f(x[j]) # Evaluamos la función f(x)
        # Si el índice es par
        elif j % 2 == 0:
            res_parcial += 2 * f(x[j])
        # Si el índice es impar
        else:
            res_parcial += 4 * f(x[j])
            
    res_final = (h / 3) * res_parcial
    return res_final 

# 3. Cálculo y Comparación
valor_aproximado = simpson_compuesto(f, a, b, n)
error_absoluto = abs(valor_exacto - valor_aproximado)

print("RESULTADOS CON n =", n)
print("Valor Exacto =", valor_exacto)
print("Valor Aproximado =", valor_aproximado)
print("Error Absoluto =", error_absoluto)