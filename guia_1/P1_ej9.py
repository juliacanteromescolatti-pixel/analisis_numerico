p = 2
coef = [9, -5, 0, 2, 9, 4, 2, 4, 7, 8, 1,6]

def horn(coef, p):
    res = p*coef[0]+coef[1]
    for i in range(len(coef)-2):
        # print(i+2,coef[i+2])
        res=p*res+coef[i+2]
    # print(res)
    return res

def horn_mal(coef, p):
    res = 0
    for i in range(len(coef)):
        res = res + coef[i]*p**(len(coef)-1-i)
    return res


print(horn(coef,p))
print(horn_mal(coef,p))
"""Lo que  hacemos en este ejercicio es , dados los coeficientes de nuestro polinomios,
tomameos como res al resultado de hacer p por el coef cero( que es el de mas valor)mas el sigiente
 (todo esto gracias a enterder Hornes) luego notamos que podemos ahorarnos dos operaciones
 por eso es i+2, pues la primera esta fija y por Horner nos ahorramos la otra.
 Luego comprobamos que el resultado que nos da el es correcto haciendo en la caluladora"""