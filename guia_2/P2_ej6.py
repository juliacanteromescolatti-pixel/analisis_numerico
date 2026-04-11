def fun_lab2ej6(x):
    y = x**(x-1)
    return y

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


ripf(fun_lab2ej6, 0.1, 1e-8, 200)