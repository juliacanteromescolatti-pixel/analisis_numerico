"""Fun es una funcion que dado x retonra f(x) y df(x) (no la defino pues rnewton recibe fun como argumento,),
 x0 es un pto inicial,err es la toleracia deseada del error, mit es el nro maximo de iteraciones permitidas"""
def rnewton (fun,x0,err,mit):
    hx = []  # historial de x
    hf = []  # historial de f(x)
# Paso inicial
    fx, dfx = fun(x0)  #dfx: derivada de f(x)
    v = fx
#ahora a cada lista le agrego x0 en el caso de hx y v a hy
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

#cCONDICIONES PARA PARAR LAS ITERACIONES:
        if abs(w) < err or abs(x1 - x0) < err:     #Son condiciones de parada (cuándo dejar de iterar)
            return (hx, hf)
#abs(w) < err: significa que encontre donde la funcion f(x) es aprox cero, es decir la raiz.
#abs(x1 - x0) < err: significa que el cambio de iteraciones es muy chico, es decir que convergio.
        
#ACTUALIZAMOS:        
        x0 = x1 # me muevo al nuevo punto
        v = w  # me muevo al nuevo puntos
    return (hx, hf)