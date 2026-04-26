"""
Actividad 1, escribir metodo de la secante (sin la derivada de newton) para una funcion f
donde la funcion debe llamarse rsecante con los parametos de entrada (fun,x0,x1,err,mit)
donde xx0 y x1 son los puntos iniciales, err el error y mit numero maximo de iteraciones
"""
#defino funcion auxiliar para intercambio de variables
def swap(x,y):
    return y,x

def rsecante(fun,x0,x1,err,mit):
    f_x0 = fun(x0)
    f_x1 = fun(x1)
    hx = []
    hy = []

#criterio maximo numero de iteraciones 
    for _ in range(mit):
        if abs(f_x0)<abs(fx1):
            x0, x1 = swap(x0,x1)
            f_x0, f_x1 = swap(f_x0, f_x1)
        s = (x1 - x0)/ (f_x1,f_x0)
        
        x1=x0
        f_x1 = f_x0
       
        x0 = x0- f_x0 * s #metodo secante
        f_x0 = fun(x0)
    
        hx.appemd(x0)
        hf.append(f_x0)
    
#el otro criterio de parada es ver si abs de f(x0) es menor que el error
        if abs(f_x0)<err:
            return hx,hf
    return hx,hf
          