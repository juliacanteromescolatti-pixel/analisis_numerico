import numpy as np
"""Act 6: Comparacion de metodo de rtaices:
Resolvé: e**(-x) = x
Usando: Bisección y Newton
Compará número de iteraciones y velocidad de convergencia."""
 #Llamaremos a los metodos de BIseccion y Newton que ya hicimos:
#Metodo de Biseccion
def rbisec(fun, I, err, mit):
    hx=[]
    hf=[]
    a = I[0]
    b = I[1]
    
    u = fun(a)
    v = fun(b)
    if u*v>0:
        print('No se cumplen las hipotesis')
        return 
    for k in range(1,mit+1):
#definimos el c en esta instancia del codigo porque a partir de ahora lo necesitamos, si no  se lo deberiamos refrescar a python
        c = a + (b-a)/2
        w = fun(c)
        hx.append(c)
        hf.append(w)
        if abs(w)<err or k>=mit: #no seria con las raices?
            return(hx, hf)
        if w*u<0:
            v=fun(c)
            b=c
        else:
            a=c
            u = fun(a)
           
    return(hx, hf)

#Metodo de Newton 
def rnewton (fun,x0,err,mit):
    hx = []  # historial de x
    hf = []  # historial de f(x)
#Paso inicial
    fx, dfx = fun(x0)  #dfx: derivada de f(x)
    v = fx
#Ahora a cada lista le agrego x0 en el caso de hx y v a hy
    hx.append(x0)
    hf.append(v)
#Ahora aplicamos las condiciones:
    for k in range(1, mit+1):
        if dfx == 0:
            print("Derivada nula")
            return (hx, hf)

#FROMULA DE NEWTON:
        x1 = x0 - v / dfx 

#EVALUAMOS EN EL NUEVO PUNTO (X1):
        w, dfx = fun(x1)

        hx.append(x1)
        hf.append(w)

#CONDICIONES PARA PARAR LAS ITERACIONES:
        if abs(w) < err or abs(x1 - x0) < err:     #Son condiciones de parada (cuándo dejar de iterar)
            return (hx, hf)
#abs(w) < err: significa que encontre donde la funcion f(x) es aprox cero, es decir la raiz.
#abs(x1 - x0) < err: significa que el cambio de iteraciones es muy chico, es decir que convergio.
        
#ACTUALIZAMOS:        
        x0 = x1 # me muevo al nuevo punto
        v = w  # me muevo al nuevo puntos
    return (hx, hf)

#Defino mi funcion:
#Como e**(-x) = x, entonces f(x) = np.exp(-x) - x
# Para bisección
def f(x):
    return np.exp(-x) - x

# Para Newton (devuelve función y derivada)
def f_newton(x):
    fx = np.exp(-x) - x
    dfx = -np.exp(-x) - 1
    return fx, dfx

# EJECUCIÓN=

# Bisección en [0,1]
hxsshf = rbisec(f, [0, 1], 1e-6, 100)

# Newton con x0 = 0.5
hx, hf = rnewton(f_newton, 0.5, 1e-6, 100)


# RESULTADOS

print("Raíz (Bisección):", hx[-1])
print("Iteraciones (Bisección):", len(hx))

print("Raíz (Newton):", hx[-1])
print("Iteraciones (Newton):", len(hx))