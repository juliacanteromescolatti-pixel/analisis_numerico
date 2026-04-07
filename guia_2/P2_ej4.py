# act 4

""" definimos en vez de una funcion auxiliar
a f como nos pide el ejercicio """
a = float(input("Ingrese un valor positivo para la variable a: "))
def fun(x):
    f = (x**3)-a
    df = 3*(x)**2
    return f, df

from P2_ej3 import rnewton
if a > 0:
    hx, hf = rnewton(fun, 1, 10e-6, 100)
    print(hx[-1])
else:
    print("no sabes leer, no cumple las hipotesis del problema !!!")
#pedimos la longitud del intervalo, es indistinto si pido hx o hf





