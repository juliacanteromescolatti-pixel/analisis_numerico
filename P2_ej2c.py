#inciso C
#primero para la funcion del inciso a
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 3, 120)
# para np.linspace, los dos primeros terminos del parentesis son el intervalo y el ultimo es la precision con la que quiero graficar, mientras mas alto mas precision
def fun (x):
    return np.tan(x)-2*x
from P2_ej1 import rbisec    
plt.plot(x, fun(x))
hx, hf = rbisec(fun, [0.8,1.4], 1e-5, 100)
plt.plot([hx],[hf],'*')
plt.legend(["trigonometrica", "par de puntitos"])
plt.show()
"""
# para la funcion del inciso b
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 3, 120)
# para np.linspace, los dos primeros terminos del parentesis son el intervalo y el ultimo es la precision con la que quiero graficar, mientras mas alto mas precision
def fun_lab2ej2b(x):
    return (x**2)-3
# no pongo math. ni np. pq no hace falta una libreria para utilizar la funcion
from P2_ej1 import rbisec    
plt.plot(x, fun_lab2ej2b(x))
hx, hf = rbisec(fun_lab2ej2b, [1,2], 1e-5, 100)
plt.plot([hx],[hf],'*')
plt.legend(["raiz", "par de puntitos"])
plt.show()
