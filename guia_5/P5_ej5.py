
#Act5
import numpy as np
import math as ma
from scipy.integrate import quad

def fun_a(x):
	y = np.exp(-1*(x**2))
	return y

resultado, error_estimado = quad(fun_a, -np.inf, np.inf )

print("El resultado del inciso a es:", resultado) 


def fun_b(x):
	y = x**2*ma.log(x+np.sqrt(x**2 + 1))
	return y

resultado, error_estimado = quad(fun_b, 0, 2)

print("El resultado del inciso b es:", resultado) 
