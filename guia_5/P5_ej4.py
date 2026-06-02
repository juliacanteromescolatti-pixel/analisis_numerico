# ACT 4 
import numpy as np
from P5_ej1 import intecomp

# funcion para integrar con tolerancia

def int_t(fun, a, b, regla:str):
	tol = 10**(-5)
	n = 2
	i_vieja = intecomp(fun, 0, 1, n, regla)
	while True:
		n = 2*n
		i_nueva = intecomp(fun, 0, 1, n, regla)
		err = abs(abs(i_vieja)-abs(i_nueva))
		if err < tol:
			return i_nueva, n, err
		i_vieja = i_nueva
		

		
def fun_a(x):
	y = x*np.exp(-x)
	return y
def fun_b(x):
	y = x*np.sin(x)
	return y
def fun_c(x):
	y = (1+x**2)**1.5
	return y
	
print()
print("Punto a con Simpson", int_t(fun_a, 0, 1, "simpson"))
print("Punto a con Trapecio", int_t(fun_a, 0, 1, "trapecio"))
print()
print("Punto b con Simpson", int_t(fun_b, 0, 1, "simpson"))
print("Punto b con Trapecio", int_t(fun_b, 0, 1, "trapecio"))
print()
print("Punto c con Simpson", int_t(fun_c, 0, 1, "simpson"))
print("Punto c con Trapecio", int_t(fun_c, 0, 1, "trapecio"))
