# act 3 p3
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 1/x
    return y
    
from P3_ej2 import inewton 
from P3_ej1 import ilagrange 
#nodos
j = np.arange(1, 102)
z_nodes = (24+j)/25
y_nodes = f(z_nodes)

#puntos para graficar
x_plot = np.linspace(1, 5, 400)

#evaluaciones
f_vals = f(x_plot)
x = np.array([1,2,3,4,5])
y = f(x)
p_vals = inewton(x, y, z_nodes)

#grafico newton
plt.figure(figsize = (8,5))
plt.plot(x_plot, f_vals, label="f(x) = 1/x")
plt.plot(z_nodes, p_vals,"--", label="plonomio interpolatorio") #z es el termino de entrada de newton
plt.plot(x,y, 'o', label='nodos') #x e y son los puntos donde interpola
plt.title("usando newton")
plt.legend()
plt.grid() #cuadriculado del grafico
plt.show()

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

