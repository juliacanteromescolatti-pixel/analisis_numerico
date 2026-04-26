"""
Intento de codigo de grafico de funciones
"""
import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(a, b, 200)
# para np.linspace, a y b son el intervalo [a,b] y el ultimo termino es la precision con la que quiero graficar, mientras mas alto mas precision  

plt.plot(x, func 1, '-.', label='nombre de mi funcion 1')
plt.plot(x, func 2, '--', label='nombre de mi funcion 2')
plt.plot(x, func 3, label='nombre de mi funcion 3')

plt.scatter(x, y, color="violet") # es un tipo de grafico que une los (x,y) con puntos, por eso pedimos muchos para tener mas presicion
plt.plot(x, y, color="blue") # es un tipo de grafico que une los (x,y) mediante rectas
#plt.plot([lista 1],[lista 0],'*') pongo los elementos de mi lista como estrellitas sobre el grafico, puedo hacer que szean puntitos cambiando por 'o' 

plt.legend() # no le ponemos nada  adentro porque ya definimos el nombre de nuestras funciones en las lineas 10, 11 y 12
plt.grid() #cuadriculado del fondo
plt.title("Titulo de mi grafico")
plt.show()

