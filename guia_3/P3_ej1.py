# act 1 pract 3

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
                
""" 
ACLARACION DE LOS FOR
el primero lo usamos pq al tener muchas z's 
tengo que calcular la funcion para cada una

el segundo es para la sumtoria

el tercero para la productoria
"""



