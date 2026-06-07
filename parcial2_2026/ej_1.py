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

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]
z = np.linspace(0, 12, 100)
altura_simpson = inewton(x, y, z)

#Aplicamos la fomula de simpson compuesta a nuestro pol obtenido

h = (12-0)/100 # intervalo de simpson es (b-a)/n
res_parcial = 0 #empiezo con un resultrado parcial igual a cero
for j in range(len(altura_simpson)):
    if j == 0 or j == len(altura_simpson):
        res_parcial += altura_simpson[j] # += acualizo el termino que tenia, es decir que voy sumando lo que voy obteniedno
    elif j%2 ==0:
        res_parcial += 2*altura_simpson[j] #sumo todos los terminos pares
    else:
        res_parcial += 4*altura_simpson[j] #sumno terminos impares
res_final = h/3 * (res_parcial) #area 

#Calulamos el area total:
volumen = res_final*10
print("area =", volumen)

#Grafico:
plt.plot(x, y, "o")
plt.title("puntos de la lista dada")
plt.show()