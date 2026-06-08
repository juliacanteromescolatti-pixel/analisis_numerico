"""Resolver: un sistema deecuaciones con el metodo de Gauss-Seidel y Jacobi
Comparar: número de iteraciones y tiempo de ejecución"""

import numpy as np
import time

# Datos del problema
A = np.array([[5.0, 1.0, 1.0], [1.0, 6.0, 1.0], [1.0, 1.0, 7.0]], dtype=float)

b = np.array([7.0, 9.0, 10.0], dtype=float)
x0 = np.zeros(3)      # Punto inicial común (0, 0, 0)
tol = 1e-6            # Tolerancia para el criterio de parada
max_iter = 100        # Máximo de iteraciones permitido


def jacobi(A, x, b, err, mit):
    z = len(b)
    u = np.zeros(z)
    x = np.array(x, dtype=float) # Aseguramos que sea un array independiente
    
    for k in range(mit):
        for i in range(z):
            n = 0
            h = 0
            for j in range(i):
                m = A[i,j] * x[j]
                n = m + n
            for j in range(i+1, z):
                r = A[i,j] * x[j]
                h = r + h
            u[i] = (b[i] - n - h) / A[i,i]
            
        # Criterio de parada
        if np.sqrt(np.dot(u - x, u - x)) < err:
            return u, k + 1 # Retornamos la solución y las iteraciones reales
            
        x = u.copy() 
        
    return x, mit

def gauss_s(A, x, b, err, mit):
    z = len(b)
    x = np.array(x, dtype=float)
    
    for k in range(mit):
        u = x.copy() # Al empezar la iteración, u tiene los valores actuales
        for i in range(z):
            n = 0
            h = 0
            for j in range(i):
                m = A[i,j] * u[j] # Usa los valores ya actualizados de esta vuelta
                n = m + n
            for j in range(i+1, z):
                r = A[i,j] * x[j] # Usa los valores de la iteración anterior
                h = r + h
            u[i] = (b[i] - n - h) / A[i,i]
            
        if np.sqrt(np.dot(u - x, u - x)) < err:
            return u, k + 1
            
        x = u.copy() 
        
    return x, mit


#Medicion de tiempo y comparacion:
#Ejecución de Jacobi
inicio_j = time.perf_counter()
sol_j, iter_j = jacobi(A, x0, b, tol, max_iter)
fin_j = time.perf_counter()
tiempo_j = fin_j - inicio_j

#Ejecución de Gauss-Seidel 
inicio_gs = time.perf_counter()
sol_gs, iter_gs = gauss_s(A, x0, b, tol, max_iter)
fin_gs = time.perf_counter()
tiempo_gs = fin_gs - inicio_gs


print("COMPARACIÓN DE MÉTODOS:")
print()
print("MÉTODO DE JACOBI:")
print("Solución =", sol_j)
print("Iteraciones necesarias =", iter_j)
print("Tiempo de ejecución en segundos =", tiempo_j)
print()
print("MÉTODO DE GAUSS-SEIDEL:")
print("Solución =", sol_gs)
print("Iteraciones necesarias =", iter_gs)
print("Tiempo de ejecución en segundos =", tiempo_gs)
	
					