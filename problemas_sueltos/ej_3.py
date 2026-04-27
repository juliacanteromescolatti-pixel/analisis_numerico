import matplotlib.pyplot as plt
"""Act 3: Método de bisección básico
Implementá bisección para encontrar una raíz de:
f(x)= x**3 -2*x -5 en el intervalo [2,3].
Graficá la función y los puntos generados."""

#Copiamos el metodo de Biseccion ya hecho
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
I = [2, 3]
err = 1e-5
mit = 100

def fun(x):
    return x**3 -2*x -5

rbisec(fun, I, err, mit)
hx,hf = rbisec(fun, I, err, mit)
print(hx,hf)
print(len(hx),len(hf))

# Graficar
plt.plot(hx, hf)
plt.grid(True, linestyle='--', color='gray', alpha=0.7) #para el cuadriculado
plt.show()
print(hx)