# act 2 p3
# se calculan los cocientes usando diferencias divididas

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
    
