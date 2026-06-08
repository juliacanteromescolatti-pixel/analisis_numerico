"""Eliminación Gaussiana: Programar:
egauss(A,b) sin usar funciones de resolución de NumPy.
Resolver un sistema 4×4 generado por vos. Verificar la solución con: numpy.linalg.solve"""

import numpy as np

# 1. Función corregida (Se eliminó la 'n' de los parámetros)
def egauss(A, b):
    # Hacemos copias para no romper las matrices originales fuera de la función
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    
    #TRIANGULACIÓN
    for k in range(n-1):
        print("k =", k)
        print("pivote =", A[k,k])
        
        for i in range(k+1, n):
            if A[k,k] == 0:
                print("ERROR: Pivote es cero. El método requiere pivoteo.")
                return None
            else:
                m = A[i,k] / A[k,k]
        
            for j in range(k, n):
                A[i,j] = A[i,j] - m * A[k,j]
                
            b[i] = b[i] - m * b[k]
            
    #SUSTITUCIÓN HACIA ATRÁS
    x = np.zeros(n) # Vector para guardar las incógnitas despejadas
    
    # Vamos de la última fila (n-1) hasta la primera (0) de atrás para adelante
    for i in range(n-1, -1, -1):
        suma = 0.0
        for j in range(i+1, n):
            suma += A[i,j] * x[j]
        x[i] = (b[i] - suma) / A[i,i]
        
    return x # Ahora sí devolvemos el vector solución con las respuestas x

# Creamos una matriz A cualquiera 4x4 y un vector b
A_sistema = np.array([[2.0,  1.0, -1.0,  2.0], [4.0,  5.0, -3.0,  6.0], [-2.0, 5.0, -2.0,  6.0], [4.0, 11.0, -4.0,  8.0]])
b_sistema = np.array([5.0, 9.0, 4.0, 2.0])

# Resolución y Verificación
# Resolvemos usando el algoritmo programado a mano
solucion_manual = egauss(A_sistema, b_sistema)

# Resolvemos usando la función oficial de NumPy para verificar
solucion_numpy = np.linalg.solve(A_sistema, b_sistema)


print("Solución obtenida con egauss() =", solucion_manual)
print("Solución obtenida con np.linalg.solve() =", solucion_numpy)

#Usamos np.allclose para comparar vectores de coma flotante
if np.allclose(solucion_manual, solucion_numpy):
    print("Las soluciones son idénticas.")
else:
    print("Hay diferencias entre los resultados.")