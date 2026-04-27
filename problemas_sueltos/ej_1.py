import numpy as np
"""Act 1: Evaluación numérica y precisión
Escribí dos funciones para calcular:
f(x)= sqrt(x**2 + 1) - 1
y una versión algebraicamente equivalente más estable.
Compará resultados para x=10−k, con k=1,…,10."""

# Defino mi funcion original tal cual como es
def fun(x):
    return np.sqrt(x**2 + 1) - 1

#Para buscar una version algebraica mas estable racionalizaremos mi funcion original
def fun_mejor(x):
    return x**2 / (np.sqrt(x**2 + 1) + 1)

#Comparemos ambas funciones, como mi k  es de (1,...,10) valuo hasta 111 para poder obtener el valor en 10
for k in range(1, 11):
    x = 10**(-k)
    
    val1 = fun(x)
    val2 = fun_mejor(x)
    
    print("k =", k)
    print("original =", fun(x))
    print("mejorada =", fun_mejor(x))
    print("valor de fun =",val1)
    print("valor de fun_mejor =",val1)

#Calculemos cual seria el error relativo que obtenemos al apriximar mi funcion con esta fun_mejor
error_relativo = abs(val1 - val2) / abs(val2)
print("error relativo =", error_relativo)