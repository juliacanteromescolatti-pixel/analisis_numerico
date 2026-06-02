#Act 6: Comparar las soluciones dadas por soleg y sollu al resolver Ax = b con:
import numpy as np

from P6_ej4 import soleg
from P6_ej5 import sollu

#A = np.array([[ 4,-1, 0,-1, 0, 0], [-1, 4,-1, 0,-1, 0], [ 0,-1, 4, 0, 0,-1], [-1, 0, 0, 4,-1, 0], [ 0,-1, 0,-1, 4,-1], [ 0, 0,-1, 0,-1, 4]])

A = np.array([[ 4,-1, 0,-1, 0, 0],
              [-1, 4,-1, 0,-1, 0],
              [ 0,-1, 4, 0, 0,-1],
              [-1, 0, 0, 4,-1, 0],
              [ 0,-1, 0,-1, 4,-1],
              [ 0, 0,-1, 0,-1, 4]])

#Realizamos lo que nos pide el ejercicio con b1:

print("Realizamos lo que nos pide el ejercicio con A y b1")
b1 = np.array([[1], [1], [1] ,[0], [0], [0]])

x_soleg = soleg(A,b1)
x_sollu = sollu(A,b1)

print("Solución con eliminación gaussiana:")
print(x_soleg)

print("Solución con LU:")
print(x_sollu)

#Podemos calcular la diferencia:
print("Norma de la diferencia:")
print(np.linalg.norm(x_soleg - x_sollu))
print()

#Realicemos el mismo porceso con b2:
print("Ahora relizamos el mismo proceso con A y b2")
b2 = np.array([1,1,1,1,1,1])

x1 = soleg(A.copy(), b1.copy())
x2 = soleg(A.copy(), b2.copy())

print("Solución con eliminación gaussiana:")
print(x_soleg)

print("Solución con LU:")
print(x_sollu)

print("Norma de la diferencia:")
print(np.linalg.norm(x_soleg - x_sollu))