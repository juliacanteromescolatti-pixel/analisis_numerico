#act 3
    
#iteraciones=mit
def fun(x):
    f= -(x**2)+1
    df = -2*x
    return f, df
"""
cuando llamo a rnewton pongo (ej.fun, x0, err, mit) con
los otros parametros a eleccion, por ej: 
x0= 2
mit=100
err= 0.5
"""
def rnewton(fun, x0, err, mit):
    hx=[] # define mi dominio
    hf=[] # define mi imagen
    f, df = fun(x0)
    hx.append(f)
    hf.append(df)
    #agregamos los elementos a las listas    
    if abs(f)<err:
        print('Ya estas muy cerca de la raiz, se cumplen las condiciones :) ')
        return (hx, hf)
    for k in range(1,mit+1):
        if df == 0:
            print("la derivada es nula, por lo que no podemos continuar")
            return (hx, hf)
        x1 = x0-f/df #f prima
        f, df = fun(x1)
        hx.append(x1)
        hf.append(f)
        if abs((x1 - x0)/x1) < err  or abs(f)<err: # pido error relativo
            return(hx, hf)
        
    print('Alcanzado el máximo de iteraciones')      
    return(hx, hf)
    
