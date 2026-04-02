p = 2
coef = [1, -5, 6, 2]

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
""" Lo que  hacemos en este ejercicio es , dados los coeficientes de nuestro polinomios,
tomameos como res al resultado de hacer p por el coef cero( que es el de mas valor)mas el sigiente
 (todo esto gracias a enterder Hornes) luego notamos que podemos ahorarnos dos operaciones
 por eso es i+2, pues la primera esta fija y por Horner nos ahorramos la otra, es decir, 
 fijamos una operacion que es la que vamos a repetir durante todo el metodo de Horner,
y la otra sale por la propia def de este metodo (ya que nos dice que si yo tengo n coeficinetes 
aplicandolo voy a tener n-1)
 Luego comprobamos que el resultado que nos da el es correcto haciendo que:
 una vez que al pol lo tenemos escrito por Horner lo calulamos con la caluladora y deeria dar lo mismo que este codigo"""