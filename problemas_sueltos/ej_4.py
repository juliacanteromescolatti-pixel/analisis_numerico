"""Act 4: Horner vs evaluación directa
Evaluá el polinomio: p(x)=x**5 - 3*x**4 + x**3 - x + 1
en x=1.0001 usando: fórmula directa y método de Horner
Compará precisión (error abs)."""

#Metodo de Horner que usaremos
def horn(coefs, x0):
    n = len(coefs)
    b = coefs[0]
    for i in range(1,n):
        b = coefs[i] + b * x0
    
    return b
#Valuamos el polinomio en forma directa
def p(x):
    return x**5 - 3*x**4 + x**3 - x + 1

valor_directo = p(1.001)
#print(valor_directo)

#Valuamops el polinomio con el metodo de Horner
horn([1, -3, 1, 0, -1, 1], 1.001) 
valor_horner = horn([1, -3, 1, 0, -1, 1], 1.0001)
#print(valor_horner)

#Imprimimos el valor del polinomio con cada metodo y cual es el error abs 
print("Directo:", valor_directo)
print("Horner:", valor_horner)
print("Error abs:", abs(valor_directo - valor_horner))