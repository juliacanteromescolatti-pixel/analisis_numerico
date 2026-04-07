# act 5 met pto fijo
#mit son iteraciones
# err tolerancia de error
def fun(x):
    y = (x**2)
    return y
"""la de arriba es  mi funcion de prueba"""


def ripf(fun, x0, err, mit):
    hx=[] # define mi dominio
    f= fun(x0)
    hx.append(x0)
    #agregamos los elementos a las listas
    x = x0
    k = 1 # k seria nuestro "contador"
    while k<=mit:
        x = fun(x0)
        print("iteracion ", k,": ", x)
        if abs(x-x0) < err: # pido error absoluto
            print("La funcion converge !!! :)")
            return hx
        k = k + 1
        x0 = x 
        hx.append(x0)
    print("Oh! haz alcanzado el maximo de iteraciones")
    return hx
        
        
    
