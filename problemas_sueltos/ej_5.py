import matplotlib.pyplot as plt
""" Act5: Interpolación simple
Dado: x = [0, 1, 2]
      y = [1, 3, 2]
Construí el polinomio interpolante de Lagrange y evalualo en 100 puntos.
Graficá puntos originales + interpolación."""

#Usaremos el codigo de interpolacion de Lagrange ya hecho
def ilagrange(x,y,z):
    n = len(x)
    m = len(z)
    w=[]
    if len(x) != len(y): 
        print("Ojo, las dimensiones de x e y son distintas, agrergar mas elementos")
    else:  #armamos el if pidiendo la misma long pq las dos pertenecen a r**n
        print("x e y son vectores de igual dimension")
        for k in range(m):
            p = 0
            for i in range(n):
                li = 1
                for j in range (n): #recorre todos los puntos de xj con j los elementos de nuestra lista
                    if j != i:
                        li =(z[k]-x[j])/(x[i]-x[j])*li
                p = p+y[i]*li
            w.append(p)
        return w
    

x = [0, 1, 2]
y = [1, 3, 2]

# puntos donde evaluar
z = []
for i in range(100):
    z.append(0 + (2 - 0) * i / 99) #
"""divido el intervalo [0,2] en 99 partes iguales” pues mi intervalo (x) va de cero a dos y 
me piden 100 ptos de iteracion, ahora Si quiero (n) puntos
en ([a,b]) incluyendo los extremos, el paso es ((b-a)/(n-1))"""
# evaluar
w = ilagrange(x, y, z)

#Graficar
plt.plot(z, w)
plt.scatter(x, y)
plt.grid(True, linestyle='--', color='gray', alpha=0.7)
plt.show()