# act 7- p3

"""
vamos a tener iuna funcion auxiliar fun, para la prueba. Y otra func 
no se como se llama del programa en si
"""

def fun(x):
   y = x**3 + x + 1
   dy = 3*x**2+1
   return y, dy
from scipy.interpolate import interp1d
from P2_ej3 import rnewton 
def rintep(fun, x0, x1, x2, err, mit):
    x= [x0,x1,x2]
    for k in range(mit):
        x = x[len(x)-3:len(x)]
        
        f =[fun(xi)[0] for xi in x] 
     
        y = f

        for i in range(3):
            if abs(y[i])<err:
                return x[i]
# Para buscar los ceros de nuesdtra fucion usaremkmos el metodo de Newton hecho en el lab2
#uso newton desde Xn+1
        p = interp1d(x,y)
        hx, hf = rnewton(fun, x[-1], err, mit) #raiz de p
        x_n =hx[-1] 
        x.append(x_n) 
        
raiz = rintep(fun, 1.0, 2.0, 3.0, 1e-6, 10)
print(raiz)
    
""" MEJORAR"""  
    
 
    
    
    
    
    

