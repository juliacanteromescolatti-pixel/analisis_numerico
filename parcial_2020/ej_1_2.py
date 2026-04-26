import math
#DEFINIMOS EL METODO DE NEWTON QUE SERA UTILIZADO EN LA ACTIVIDAD DOS
def rnweton(fun, x0, err, mit):
    f_x0, df_x0 = fun(x0)

    hx = [x0]
    hf = [f_x0]
    
    if abs(f_x0) < err:
        return hx, hf
    
    for _ in range(mit):
        xn = x0 - f_x0/df_x0
        f_xn, df_xn = fun(xn)

        hx.append(xn)
        hf.append(f_xn)

        if ((abs(xn-x0)/abs(xn))<err) or (abs(f_xn)<err):
            return hx, hf
        
        x0 = xn
        f_x0= f_xn
        df_x0 =df_xn
    
    return hx, hf
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
    hf = []

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
            return hx, hf #me devuelve la historia de ptos y la funcion valuada en los ptos
        
#Si no frena porque el valor absoluto de la funcion en el pto es menor que el error, frenara por maximo de iteraciones
    return hx, hf
          

"""
Actividad 2, implementar funcion llamada busquqeda cero que tenga los
mismos parametros de entrada del pto anterior, y que aplique el metodo de newton con pto inicial x0,
y de la secante sobre la funcion fun. Debemos imprimir las raices con cada metodo,
el numero de iteraciones que le lleva acada metodo para llegar a cero.
Y debe retornar el pto para el cual el valor abs de la funcion es el cero mas cercano.
"""
def busqueda_ceros(fun, x0, x1, err, mit):
    hx_newton, hf_newton = rnweton(fun, x0, err, mit)
    hx_secante, hf_secante = rsecante( lambda x : fun(x)[0], xo, x1, err, mit) #en vez de fun, uso lamda de x tq solo me da el primer elemneto de la fun, pues rsecante solo usa el valor de fun, no de la derivada
    
    print(f"La aproximacion a la raiz encontrada con el metodo de Newton es {hx_newton[-1]}.") #uso [-1] pues es el ultimo elemneto de la lista
    print(f"El numero de iteraciones realizadas es de {len(hx_newton)}.") #calulo la longitud de la lista para la cant de iteraciones

    print(f"La aproximacion a la raiz encontrada con el metodo de la Secante es {hx_secante[-1]}.")
    print(f"El numero de iteraciones realizadas es de {len(hx_secante)}.")

#Buscamos el cero mas cercano al valor absluto de la funcion
#COmpara las ultimos elementos de Nweton y de la Secante y veo cual es el mas chico con respecto a abs(f)
    if abs(hx_newton[-1]) < abs(hf_secante[-1]):
        print(f"La aproximacion mas cercana due dada por el metodo de Newton, y es {hf_newton[-1]}.")
    else:
        print(f"La aproximacion mas cercana due dada por el metodo de la Secante, y es {hf_secante[-1]}.")
