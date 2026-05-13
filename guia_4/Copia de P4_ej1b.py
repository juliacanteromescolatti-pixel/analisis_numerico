"""(b)Realizar los mismos c´alculos con la ayuda de las funciones dot y ones (NumPy)."""
import numpy as np

datos = np.loadtxt("/home/visitante/Documentos/vj/guia_4/datos1a.dat")
x = datos[0]
y = datos[1]
v = np.ones(len(x))
sum_x = (np.dot(x,v))
sum_y = (np.dot(y,v))
sum_xc = (np.dot(x,x))
sum_xy = (np.dot(x,y))

m = len(x)

a0 = (sum_xc * sum_y - sum_xy * sum_x)/(m*sum_xc-(sum_x)**2)

a1 = (m*sum_xy-sum_x*sum_y)/(m*sum_xc-(sum_x)**2)
	
print(np.sum((y-(a1*x+a0))**2)) #esto es el cuadrado minimo

xi = [0,5]
yi = [a1*xi[0] + a0,a1*xi[1] + a0]
