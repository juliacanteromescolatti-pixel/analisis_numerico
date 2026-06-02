# act 6
import numpy as np
from P5_ej1 import intecomp


def pendulo(l, alpha:int):
	g = 9.8
	if alpha != 0:
	
		alpha_r = np.radians(alpha)
		def fun(x):
			y = 1/(1-(np.sin(alpha_r/2))**2 * (np.sin(x))**0.5)  #x es teta
			return y
		integral = intecomp(fun, 0, np.pi/2, 100, "simpson")
		T = 4*np.sqrt(l/g)*integral
		return T
	else:
		print("Si el angulo es nulo, el pendulo no tiene movimiento y por ende no tiene periodo")
