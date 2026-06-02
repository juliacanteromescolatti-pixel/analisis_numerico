#Act  1
import numpy as np

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
		x = u	
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
		x = u	
	return x,k
	
					



# salida [x, k ] con  sol aprox y k numero de iteraciones


