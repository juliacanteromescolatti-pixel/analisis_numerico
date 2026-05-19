# ACT 2
import numpy as np
# valor real de la integral es 0.632121
def fun(x):
    return np.exp(-x)
    
from P5_ej1 import intecomp
# con regla de simpson
print("SIMPSON")
print()
print ("Simpson con n=4: ", intecomp(fun,0,1,4,"simpson"))
print ("Simpson con n=10: ", intecomp(fun,0,1,10,"simpson"))
print ("Simpson con n=20: ", intecomp(fun,0,1,20,"simpson"))
S1 = intecomp(fun,0,1,4,"simpson")
S2 = intecomp(fun,0,1,10,"simpson")
S3 = intecomp(fun,0,1,20,"simpson")
Es1 = abs(0.632121-S1)
Es2 = abs(0.632121-S2)
Es3 = abs(0.632121-S3)
print("Los errores absolutos de simpson con 4, 10 y 20 subintervalos respectivamente son: ", Es1, Es2, Es3)

# con regla de trapecio
print()
print("TRAPECIO")
print()
print ("Trapecio con n=4: ", intecomp(fun,0,1,4,"trapecio"))
print ("Trapecio con n=10: ", intecomp(fun,0,1,10,"trapecio"))
print ("Trapecio con n=20: ", intecomp(fun,0,1,20,"trapecio"))
T1 = intecomp(fun,0,1,4,"trapecio")
T2 = intecomp(fun,0,1,10,"trapecio")
T3 = intecomp(fun,0,1,20,"trapecio")
Et1 = abs(0.632121-T1)
Et2 = abs(0.632121-T2)
Et3 = abs(0.632121-T3)
print("Los errores absolutos de trapecio con 4, 10 y 20 subintervalos respectivamente son: ", Et1, Et2, Et3)

# con regla de Punto Medio
print()
print("PUNTO MEDIO")
print()
print ("Punto medio con n=4: ", intecomp(fun,0,1,4,"pm"))
print ("Punto medio con n=10: ", intecomp(fun,0,1,10,"pm"))
print ("Punto medio con n=20: ", intecomp(fun,0,1,20,"pm"))
P1 = intecomp(fun,0,1,4,"pm")
P2 = intecomp(fun,0,1,10,"pm")
P3 = intecomp(fun,0,1,20,"pm")
Ep1 = abs(0.632121-P1)
Ep2 = abs(0.632121-P2)
Ep3 = abs(0.632121-P3)
print("Los errores absolutos de Punto Medio con 4, 10 y 20 subintervalos respectivamente son: ", Ep1, Ep2, Ep3)


