#Resolver con soltrsup(A,b) un sistema triangular superior 
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
A = np.array([[2, 0, 0], [1, 4, 0], [3, 2, 5]])

b = np.array([[10], [8], [15]])

x = soltrsup(A, b)
print("Solucion para una matriz triang sup: ", x)
print()
