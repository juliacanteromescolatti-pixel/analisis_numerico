def rsteffensen (fun,x0,err,mit):
    hx = []  # historial de x
    hf = []  # historial de f(x)
#Paso inicial
    fx = fun(x0)  
    v = fx
#Ahora a cada lista le agrego x0 en el caso de hx y v a hy
    hx.append(x0)
    hf.append(v)
#Ahora aplicamos las condiciones:
    for k in range(1, mit+1):
        denominador = fun(x0 + fun(x0))-fun(x0)
        print(f"Denominador paso {k}: {denominador}")
        if denominador == 0:
            print("Denominador nulo")
            return (hx, hf)

#FROMULA DE STEFFENSEN:
        x1 = x0 - (fun(x0)**2)/denominador

#EVALUAMOS EN EL NUEVO PUNTO (X1):
        w = fun(x1)

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