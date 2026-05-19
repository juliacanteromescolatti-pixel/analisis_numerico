# ACT 3
"""
Antes de llamar a la funcion ene la taerminal, importamos numpy o math
y valuamos senint_[tipo]([0,np.pi/2,np.pi])
"""
import numpy as np
import matplotlib.pyplot as plt

from P5_ej1 import intecomp
def fun(x):
	return np.cos(x)

xi=[]

def senint_ceil(x):
	yi = []
	for xi in x:    # el xi es el que recorre en x 
		if xi == 0:
			yi.append(0)
		else:
			n = int(np.ceil(xi/0.1))
			yi.append(intecomp(fun,0,xi,n,"trapecio"))
	return yi
def senint_floor(x):
	yi = []
	for xi in x:
		if xi == 0:
			yi.append(0)
		else:
			n = int(np.floor((xi/0.1)+1))
			yi.append(intecomp(fun,0,xi,n,"trapecio"))
	return yi
def senint_round(x):
	yi = []
	for xi in x:
		if xi == 0:
			yi.append(0)
		else:
			n = int(np.round(xi/0.1)+1)
			yi.append(intecomp(fun,0,xi,n,"trapecio"))	
	return yi

# GRAFICO	
"""
Cuando grafiquemos hacer MUCHO zoom sobre la funcion exacta pq se aproximan muy bien,
Ademas notar que y_floor y y_round son igual por lo que estan encimadas en el grafico
"""
x = np.arange(0, 2*np.pi+0.5, 0.5) # valores de x
y_floor = senint_floor(x)
y_ceil = senint_ceil(x)
y_round = senint_round(x)
y_exact = np.sin(x) # valor exacto de la funcion

plt.plot(x, y_round,  color="red", label='Valor de mi funcion usando Round')
plt.plot(x, y_floor, '--', color="blue", label='Valor de mi funcion usando Floor')
plt.plot(x, y_ceil, '--', color="pink", label='Valor de mi funcion usando Ceil')
plt.plot(x, y_exact, color="yellow",  label='Valor Exacto de la funcion')

plt.legend() 
plt.grid() #cuadriculado del fondo
plt.title("Aproximcion numerica de sen(x) :)")
plt.show()


