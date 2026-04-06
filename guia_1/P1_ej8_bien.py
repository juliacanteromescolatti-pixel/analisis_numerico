import math
def mala(a,b,c):
    disc=b**2-4*a*c

    if disc<0:
        print("EL dsicriminante es menor que 0, intente de nuevo")
        return None
    
    x_1=(-b+sqrt(disc))/(2.0*a)
    x_2=(-b-sqrt(disc))/(2.0*a)

    return[x_1,x_2]

def buena(a,b,c):
    disc=b**2-4*a*c

    if disc<0:
        print("EL dsicriminante es menor que 0, intente de nuevo")
        return None

#Encontrar la raiz mas lejana al cero en valor absoluto
    if b>0:
        x_1=(-b-sqrt(disc))/(2.0*a)
    else:
        x_1=(-b+sqrt(disc))/(2.0*a)
    x_2=(c/a)/x_1

    return[x_1,x_2]