# act 4 p3

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 1/(1+25*x**2)
    return y
    
from P3_ej2 import inewton 
from P3_ej1 import ilagrange 
n = 10
#puntos para graficar
x_plot = np.linspace(-1, 1, 200)

#nodos
j = np.arange(n+1)
z_nodes = np.cos(((2*j+1)/(2*n+2))*3.14)
y_nodes = f(z_nodes)
q_vals= inewton(z_nodes, y_nodes, x_plot)

#evaluaciones
f_vals = f(x_plot)
i = np.arange(1,n+2) #para poder dividir por una listra, lo escribo de esta forma
x = 2*(i-1)/n - 1
y = f(x)
p_vals = inewton(x, y, x_plot)



#grafico newton
plt.figure(figsize = (8,5))
plt.plot(x_plot, f_vals, label="f(x) = 1/x")
plt.plot(x_plot, p_vals,"--", label="polinomio p") #z es el termino de entrada de newton
plt.plot(x_plot,q_vals, "-.", label='nodos') #x e y son los puntos donde interpola
plt.title("")
plt.legend()
plt.grid() #cuadriculado del grafico
plt.show()
'''
#grafico lagrange
p_vals = ilagrange(x, y, z_nodes)
plt.figure(figsize = (8,5))
plt.plot(x_plot, f_vals, label="f(x) = 1/x")
plt.plot(z_nodes, p_vals,"--", label="plonomio interpolatorio")
plt.plot(x,y, 'o', label='nodos')
plt.title("usando lagrange")
plt.legend()
plt.grid()
plt.show()
'''
