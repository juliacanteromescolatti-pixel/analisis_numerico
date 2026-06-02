# Act 3

import numpy as np

# TRIANG SUP
def soltrsup(A, b):
	n = len(b)
	
#Verifico la singularidad:
	if np.any(np.diag(A) == 0):
		print("Error: la matriz es singular")	
		return None

	x = np.zeros(n)

	for i in range(n-1, -1, -1): #ponemos -1 -1 pq hace que se recorran las filas desde la ultima a la primera
		suma = 0
		for j in range(i+1, n):
			suma += A[i,j]* x[j]
		
		x[i] = (b[i]-suma)/ A[i,i]
 		
	return x
 		
# MATRIZ DE PRUEBA 
A = np.array([[1, 2, 3, 1], [0, 2, 1, 4], [0, 0, 3, 2], [0, 0, 0, 5]])
 
b = np.array([[16], [15], [13], [10]])

x = soltrsup(A, b)
print("Solucion para una matriz triang sup: ", x)
print()
"""SOLUCION ESPERADA: [[1], [2], [3], [2]]"""

# TRIANG INF
def soltrinf(A, b):
	n = len(b)
	
#Verifico la singularidad:
	if np.any(np.diag(A) == 0): # el np.any hace que si se cumple que A es diagonl lo imprime(recorre de arriba hacia abajo)
		print("Error: la matriz es singular")	
		return None
 	
	x = np.zeros(n)
 	
	for i in range(n):
		suma = 0
		for j in range(i):
			suma += A[i,j]* x[j]
 			
		x[i] = (b[i]-suma)/ A[i,i]
	
	return x
	
# MATRIZ DE PRUEBA 
B = np.array([[1, 0, 0, 0], [2, 1, 0, 0], [1, 3, 2, 0], [4, 1, 2, 1]])
 
b_ = np.array([[1], [4], [11], [12]])

x_ = soltrinf(B, b_)
print("Solucion para una matriz triang inf: ", x_)
print()
"""SOLUCION ESPERADA: [[1], [2], [2], [2]]"""
