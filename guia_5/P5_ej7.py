# act 7
import numpy as np
def simpson_simple(fun, a, b):
	c = (a+b)/2
	y = ((b-a)/6)*(fun(a)+4*fun(c)+fun(b))
	return y

def simpson_adpt(fun, a , b, epsilon):	
	c = (a+b)/2
	q = simpson_simple(fun, a, b)	
	q1 = simpson_simple(fun, a, c)
	q2 = simpson_simple(fun, c, b)
	err = abs(q-q1-q2)/15

	if err < epsilon:
		return q1+q2	
	else:
	 	q1 = simpson_adpt(fun, a , c, epsilon/2)
	 	q2 = simpson_adpt(fun, c , b, epsilon/2)
	 	return q1+q2
	 	
#Funcion prueba:
def fun(x):
	y = x* np.exp(-x**2)
	return y

aprox = simpson_adpt(fun, 0, 1, 1e-6)
exacto = 0.5 * (1-np.exp(-1))

print("Aproximación =", aprox)
print("Valor exacto =", exacto)
print("Error =", abs(aprox - exacto))
	 	
'''	 
Ejemplo de recursion: de usar una funcion para definir otra	
def fac(n):
	if n==1:
		return n
	else:
		prod = n*fac(n-1)
		return prod
'''
