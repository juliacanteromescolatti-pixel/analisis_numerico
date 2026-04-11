"""nos guiamos del algoritmo del MB clase 6 del apunte pasado a lenguaje python"""
def fun(x):
    x=(I)
#iteraciones=mit
# I = [a,b]
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
    

