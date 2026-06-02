#JULIA CANTERO MESCOLATTI
#Act 2
#IMPORTAREMOS NUMPY PARA PODER USAR LA FUNCION TRIGONOMETRICA SEN(X) y MATPLOTLIB.PYPLOT PARA PODER GRAFICAR
#Llamaremos a un codigo ya realizado en clase, el Metodo de Biseccion
#INCISO A: LO QUE HAREMOS SERA DEFINIR EL METODO DE BISECCION CON NUESTRO NUEVO CK
import numpy as np
import matplotlib.pyplot as plt
def rbisec(fun, I, err, mit):
    hx=[]
    hf=[]
    ak = I[0]
    bk = I[1]
    alpha = (3 - 5**0.5)/ 2
    
    u = fun(ak)
    v = fun(bk)
    if u*v>0:
        print('No se cumplen las hipotesis')
        return 
    for k in range(1,mit+1):
#Definimos el c en esta instancia del codigo porque a partir de ahora lo necesitamos, si no  se lo deberiamos refrescar a python
        ck = alpha * ak + (1 - alpha)*bk
        w = fun(ck)
        hx.append(ck)
        hf.append(w)
        if abs(w)<err or k>=mit:
            return(hx, hf)
        if w*u<0:
            v=fun(ck)
            bk = ck
        else:
            ak =ck
            u = fun(ak)
           
    return(hx, hf)

#INCISO B:
I = [0, 2]
err = 1e-10
mit = 100

def fun(x):
    return x*np.sin(x) - 1

rbisec(fun, I, err, mit)
hx,hf = rbisec(fun, I, err, mit)
print(hx,hf)
print(len(hx),len(hf))

a = 0
b = 2
h = (b-a)/99
x = [a + i*h for i in range(100)]

#INCISO C 
plt.plot(x, fun(x), hx, hf, "o")
plt.grid(True, linestyle='--', color='gray', alpha=0.7) #para el cuadriculado
plt.title("Mi funcion y el Metodo de Biseccion")
plt.legend(["Mi funcion", "iteraciones con el Metodo de biseccion"])
plt.show()
print(hx)