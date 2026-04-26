# act 6 

import numpy as np
import matplotlib.pyplot as plt

x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([1, 2, 5, 10, 5, 2, 1])
z = np.linspace(-3, 3, 10)

j = np.arange(100) #lista del 0 al 99.
z = (-3+j/100 *6) #recorre todos los nros, de manera equidistante. entre -3 y 3
""" 
para definir z usamos la misma logica que para 
el calculo de intervalos en el met.B
a+(j/n)*(b-a)
si j=1 y n=2 es la formula de biseccion
y si j=n tenemos b
"""

from P3_ej1 import ilagrange

from P3_ej2 import inewton

from scipy.interpolate import interp1d

f_interp = interp1d(x, y)

# Para hacer el Grafico
t = np.linspace (-3, 3, 400)

y_ilagrange = ilagrange(x, y, t) 
y_inewton = inewton(x, y, t) 
y_interp = f_interp(t)


plt.plot(t, y_ilagrange, '-.', label='Pol int de Lagrange')
plt.plot(t, y_inewton, '--', label='Pol int de Newton')
plt.plot(t, y_interp, label='Funcion cubica')

plt.scatter(x, y, color="violet")

plt.legend()
plt.grid()
plt.title("Poilinomios interpolatorios para la tabla de valores :)")
plt.show()


