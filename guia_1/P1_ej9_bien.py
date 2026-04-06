def horn(coefs,x):
    n=len(coefs) # longitud de la lista de los coeficientes
    b=coefs[0] #a_n, tomo el elemneto cero de los coeficiente, que seria el a_n

    for i in range(1,n):
        b=coefs[1]+x*b #Los voy pisando, pido el ultimo b tq acumula el valor del pol en x
    return b

#EJEMPLO DE UN POL QUE AL VALUARNO EN DOS, DEBERIA DAR IGUAL A DOS:
p=horn ([1,-5,6,2],2)
print(2**3-5+2**2+6*2+2)
print(p)