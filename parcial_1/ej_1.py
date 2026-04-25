def fact(y):
    if y < 0:
        return None
    elif y == 0:
        return 1
    else:
        res = 1
        for i in range(1,y+1):
            res = res*i
        return res

def sen_taylor(n,x):
    termino = (((-1)**n)/(fact(2*n+1)))*x**(2*n+1)
    return termino

def serie_seno(x):
    resultado = 0
    terminos = []
    n = 5
    for i in range(n):
        terminos.append(sen_taylor(i,x)) #obtengo el termino i, y lo voy agregando a la lista
        resultado = resultado + terminos[i] #para obtrener el resultado, hago el rsultado inicial mas el primer termino, y asi sucecivamente
    return resultado

# print(serie_seno(1.57))