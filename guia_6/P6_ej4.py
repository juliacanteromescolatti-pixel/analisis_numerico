#Act 4

import numpy as np

"""INCISO A"""
def egauss(A, b, n):
	n = len(b)
	for k in range(n-1):
		print("k =", k)
		print("pivote =", A[k,k])
		for i in range(k+1, n):
			if A[k,k] == 0:
				print("ENTRO AL RETURN NONE")
			else:
				m  = A[i,k]/A[k,k]
			for j in range(k+1, n):
				A[i,j] = A[i,j]-m*A[k,j]
			b[i] = b[i]-m*b[k]
	return A, b
	
# FUNCION DE PRUEBA

A = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]])

b = np.array([[1], [2], [3]])

U,y = egauss(A,b,len(b))

print("La respuesta de egauss con la matriz de prueba es: ", U, y)

"""
RESPUESTA ESPERADA:

U = [[2, 1, 1], [0, 1, 1], [0, 0, 2]]

y = [[1], [0], [-1]]
"""



"""INCISO B"""
from P6_ej3 import soltrsup

def soleg(A, b):
	U,y = egauss(A,b,len(b))
	x = soltrsup(U,y)
	return x
	
# FUNCION DE PRUEBA

A = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]])

b = np.array([[1], [2], [3]])

x = soleg(A, b)

print("La respuesta de soleg con la matriz de prueba es: ", x)

"""RESPUESTA ESPERADA: [[1], [-1], [0]]"""
