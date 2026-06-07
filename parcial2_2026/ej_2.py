#Compare el comportamiento de los metodos de Jacobi y Gauss-Seidel. Utilice los siguiente puntos
#iniciales: (a) x0 = (2, 0), (b) x0 = (0.03, 0.03), (c) x0 = (0, 1).
import numpy as np

A = np.array([[1, -1], [1, 1]], dtype=float)
b = np.array([[0], [0]], dtype=float)
#X iniciales que me da el problema:
x0a = [2, 0]
x0b = [0.03, 0.03]
x0c = [0, 1] 

def jacobi(A, x:list , b, err, mit):
	z = len(b)
	u = np.zeros(z)
	
	for k in range(mit):
		for i in range(z):
			n = 0
			h = 0
			for j in range (i):
				m = A[i,j] * x[j]
				n = m + n
			for j in range (i+1, z):
				r = A[i,j] * x[j]
				h = r + h
			u[i] = (b[i]-n-h)/A[i,i]
		if np.sqrt(np.dot(u-x, u-x))<err:
			return(u, k)
		#for i in range (z):
		#	x[i] = u[i]
		x = u.copy()
	return x,k
	
def gauss_s(A, x:list , b, err, mit):
	z = len(b)
	u = np.zeros(z)
	
	for k in range(mit):
		for i in range(z):
			u[i] = 0
			n = 0
			h = 0
			for j in range (i):
				m = A[i,j] * u[j]
				n = m + n
			for j in range (i+1, z):
				r = A[i,j] * x[j]
				h = r + h
			u[i] = (b[i]-n-h)/A[i,i]
		if np.sqrt(np.dot(u-x, u-x))<err:
			return(u, k)
		#for i in range (z):
		#	x[i] = u[i]
		x = u.copy()
	return x,k

err = 1e-8
mit= 100

#INCISO A
sol_jacobi_a = jacobi(A, x0a , b, err, mit)
sol_gauss_a = gauss_s(A, x0a , b, err, mit)
print("sol_jacobi_a =", sol_jacobi_a)
print("sol_gauss_a =", sol_gauss_a)

#INCISO B
sol_jacobi_b = jacobi(A, x0b , b, err, mit)
sol_gauss_b = gauss_s(A, x0b , b, err, mit)
print("sol_jacobi_b =", sol_jacobi_b)
print("sol_gauss_b =", sol_gauss_b)

#INCISO A
sol_jacobi_c = jacobi(A, x0c , b, err, mit)
sol_gauss_c = gauss_s(A, x0c , b, err, mit)
print("sol_jacobi_c =", sol_jacobi_c)
print("sol_gauss_c =", sol_gauss_c)

#No convergen pues:
# Comportamiento de Jacobi: Verás que los valores de x simplemente se van a "turnar" 
# o ciclar en magnitudes similares (por ejemplo, alternando signos o posiciones), 
# debido a los autovalores imaginarios mas y menos i
# Comportamiento de Gauss-Seidel: Verás que debido al autovalor -1,
# los resultados experimentarán un rebote de signos iteración tras iteración,
# manteniendo la distancia inicial constante en lugar de reducirse a cero.
