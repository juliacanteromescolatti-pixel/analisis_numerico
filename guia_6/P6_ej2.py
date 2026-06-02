# Act 2
"Usar metodo de jacobi y gauss seidel"

import numpy as np
from P6_ej1 import jacobi, gauss_s

#Inciso 1:
# Crear una matriz de #[] filas y [1,2, ...,n] columnas
A = np.array([[3, 1, 1], [2, 6, 1], [1, 1, 4]])
print("La matriz A es: ")
print(A)
print()

b = np.array([[5], [9], [6]])
print("El vector b es: ")
print(b)
print()
x = np.zeros(3)
j = jacobi(A, x , b, 1e-11, 100)
g = gauss_s(A, x , b, 1e-11, 100)
print("Con gauss seidel la solucion es: ", g)
print("Con jacobi la solucion es: ", j)

A_j = A@j[0]
A_g = A@g[0]
print("Si hacemos el producto de A con la solucion de gauss seidel obtenemos: ")
print(A_j)
print()
print("Si hacemos el producto de A con la solucion de jacobi obtenemos: ")
print(A_g)

print()

#Inciso 2:
B = np.array([[5, 7, 6, 5], [7, 10, 8, 7], [6, 8, 10, 9], [5, 7, 9, 10]])
print("La matriz B es: ")
print(B)
print()

b_ = np.array([[23], [32], [33], [31]])
print("El vector b es: ")
print(b_)
print()
h = np.zeros(4)
j_ = jacobi(B, h , b_, 1e-4, 100)
g_ = gauss_s(B, h , b_, 1e-4, 100)
print("Con gauss seidel la solucion es: ", g_)
print("Con jacobi la solucion es: ", j_)

B_j = B@j_[0]
B_g = B@g_[0]
print("Si hacemos el producto de B con la solucion de gauss seidel obtenemos: ")
print(B_j)
print()
print("Si hacemos el producto de B con la solucion de jacobi obtenemos: ")
print(B_g)
