import numpy as np
"""Act 7: . Punto fijo con distintas funciones
Reescribí: x**2 - 3 = 0
Como: a) sqrt(3)
      b) 1/2 (x + 3/x)
Probá convergencia con distintos x0 y compará.
Dada la funcion x**2 - 3 = 0, el pto fijo es x = sqrt3.
Ambas funciones tienen como punto fijo la raíz de tres.
Siendo las fubnciones G1 = 3/x y G2 = (x+3/x)/2")"""

#Usaremos el codigo de pto fijo ya hecho
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


#Primera reescritura
def fun(x):
    return 3 / x

print("g1: 3/x")

ripf(fun, 0.5, 1e-6, 10)
ripf(fun, 1, 1e-6, 10)
ripf(fun, 2, 1e-6, 10)

#Segunda reescritura
def fun(x):
    return 0.5 * (x + 3/x)

print("g2: (x+3/x)/2")

ripf(fun, 0.5, 1e-6, 10)
ripf(fun, 1, 1e-6, 10)
ripf(fun, 2, 1e-6, 10)

#G1  oscila y no convrege, en cambio G2 si converge