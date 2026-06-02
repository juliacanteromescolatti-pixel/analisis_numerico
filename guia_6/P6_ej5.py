#Act :
"""La consigna dice: Resolver Ax=b usando descomposición LU con pivoteo.
Eso significa que no resolvemos directamente Ax=b, sino que primero escribimos:
PA=LU donde: P = matriz de pivoteo, L = triangular inferior, U = triangular superior"""

from scipy.linalg import lu
from P6_ej3 import soltrsup, soltrinf

# La funcion scipy.linlag,realiza la descomposición LU con pivoteo parcial de una matriz cuadrada 

def sollu(A,b):

    P, L, U = lu(A) 

    bp = P.T @ b # Que es lo mismo que b*p=P**(T)*b=P**(-1)*b. bp contiene el resultado de multiplicar P**(T) por b.

    y = soltrinf(L, bp) #Ahora tenemos Ly = bp y L es triangular inferior, entonces usamoos ej_3

    x = soltrsup(U, y) #Ahora tenemos Ux = y y L es triangular superior, entonces usamoos ej_3

    return x

"""OBS: vemos que es P, L, y U #Queremos reoslver PA=LU, entonces A=P**(-1)LU, si reemplazamps en Ax=b
tenemos (P**(-1)LU)x=b, multiplicamos por P, entonces LUx=Pb, pero la consigna escribe Ly=P**(-1)b
pero como P**(-1)=P**(T) podemos calcular lo siguiente:  bp = P.T @ b"""

#MATRIZ DE PRUEBA:
import numpy as np

A = np.array([[2,1],[1,3]])

b = np.array([[5],[6]])

x = sollu(A,b)

print(x)