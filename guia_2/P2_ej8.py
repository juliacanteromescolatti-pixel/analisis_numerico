#act 8
"""Calularemos la primera derivada para ver onde esta el minimo, y luego la segunda pues 
es la que necesitaremos al meomento de aplicar el metodo de Newton.
Porque para encontrar las raices de la primera, necesito la segunda derivada  asi aplicar el metodo."""

import numpy as np

#DEFINIMOS g(x) = f'(x) SIN EL DENOMINADOR
#    Queremos resolver g(x) = 0
def g(x):
    # x^2 * sec^2(x) - 2x * tan(x)
    return x**2 * (1/np.cos(x))**2 - 2*x*np.tan(x)


#DEFINIMOS g'(x) (derivada de g)
#    Necesaria para el método de Newton
def dg(x):
    return 2*np.tan(x) * (x**2 * (1/np.cos(x))**2 - 1)


#METODO DE NEWTON
#    f  -> función (acá g)
#    df -> derivada (acá dg)
#    x0 -> valor inicial
def newton(f, df, x0, tol=1e-8, max_iter=100):
    
    x = x0  # valor inicial
    
    for i in range(max_iter):
        
        # fórmula de Newton:
        # x_{n+1} = x_n - f(x_n)/f'(x_n)
        x_new = x - f(x)/df(x)
        
        # criterio de parada:
        # si el cambio es muy chico, terminamos
        if abs(x_new - x) < tol:
            return x_new, i+1  # devuelve raíz y cantidad de iteraciones
        
        # actualizamos el valor
        x = x_new
    
    # si no converge en max_iter
    return x, max_iter

#ELEGIMOS UN VALOR INICIAL
#    Debe estar en (0, pi/2)
x0 = 1.0
#APLICAMOS NEWTON
#    devuelve:
#    raiz -> punto crítico
#    it   -> cantidad de iteraciones
raiz, it = newton(g, dg, x0)
#DEFINIMOS LA FUNCION ORIGINAL
def f(x):
    return np.tan(x) / x**2

#MOSTRAMOS RESULTADOS
print("Punto crítico (donde f'(x)=0):", raiz)
print("Cantidad de iteraciones:", it)
print("Valor mínimo f(x):", f(raiz))