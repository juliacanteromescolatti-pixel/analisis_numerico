#Calcular el area usando la regla de simpson compuesta, interpolando los puntos con algun metodo
import matplotlib.pyplot as plt
#Usamos Newton para interpolar los puntos
def inewton(x,y,z):
    n = len(x)
    m = len(z)
    w=[]
    c = coefs(x,y)
    if len(x) != len(y): 
        print("Ojo, las dimensiones de x e y son distintas, agrergar mas elementos")
    else:  #armamos el if pidiendo la misma long pq las dos pertenecen a r**n
        print("x e y son vectores de igual dimension")
        for k in range(m):
            p = 0
            for i in range(n):
                li = 1
                for j in range (i): #recorre todos los puntos de xj con j los elementos de nuestra lista
                    li =(z[k]-x[j])*li 
                p = p+c[i]*li
            w.append(p)
        return w
#hacemos algritmo para calcular los coeficientes de la tabla de dif divididas
import numpy as np # importamos numpy y le pedim os una matriz llena de ceros
def coefs(x,y):
    n = len(x)
    c = np.zeros((n,n))
    c[:,0] = y
    for j in range(1,n):
        
        for i in range(n-j):
            
            c[i,j] = (c[i+1, j-1]-c[i, j-1])/(x[i+j]-x[i])
        
    return c[0,:]       

"""x = [0,1,2,3,4]
y = [0,1,4,9,16]
z = [0,1.5,2.5,3.5]
res = inewton(x,y,z)
print(res)"""

import numpy as np

# Datos originales del problema
x = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]

# (b) Crear la función trapecio_adaptativo para intervalos no equidistantes
def trapecio_adaptativo(x_pts, y_pts):
    integral = 0.0
    n = len(x_pts)
    
    # Recorremos par a par de puntos consecutivos
    for i in range(n - 1):
        # Base del trapecio actual (distancia variable entre x_i y x_{i+1})
        h = x_pts[i+1] - x_pts[i] #no es sobre n pues no estan equiespaciados
        
        # Área del trapecio: base * (suma de alturas) / 2
        area_trapecio = h * (y_pts[i+1] + y_pts[i]) / 2.0
        
        # Acumulamos en nuestra integral parcial
        integral += area_trapecio
        
    return integral

# (c) Calcular la cantidad aproximada de metros cúbicos
# Primero calculamos el área del perfil transversal usando tu función
area_total = trapecio_adaptativo(x, y)

# El volumen final es el área por los 10 metros de ancho del terreno
volumen = area_total * 10

print("Área aproximada del perfil =", area_total, "m²")
print("Volumen aproximada de tierra a remover =", volumen, "m³")

#Grafico:
plt.plot(x, y, "o")
plt.title("puntos de la lista dada")
plt.show()