"""escribir dos funciones para la resulucion de ecuaciones de segundo grado
del tipo ax**2+bx+c una sera mala (usando la forma tradicional)
y la otra buena (creada de manera eficiente para evitar la perdida de digitos)"""
def mala():
    a=float(input("introduzca un numero para ser el termino acompañando a x cuadrado: "))
    b=float(input("introduzca un numero para ser el termino acompañando de x: "))
    c=float(input("introduzca un numero para ser el termino independiente: "))
    dis=(b**2)-4*a*c
    if dis > 0:
        print("la funcion f tiene dos raices reales")
    elif dis < 0:
        print("la funcion f tiene dos raices complejas conjugadas")
    else:
        print("la funcion f tiene una unica raiz") 
    x1 = (-b+dis**0.5)/(2*a)
    x2 = (-b-dis**0.5)/(2*a)
    return x1, x2

# ahora armamos la mala
def buena():
    a=float(input("introduzca un numero para ser el termino acompañando a x cuadrado: "))
    b=float(input("introduzca un numero para ser el termino acompañando de x: "))
    c=float(input("introduzca un numero para ser el termino independiente: "))
    dis=(b**2)-4*a*c
    if dis > 0:
        print("la funcion f tiene dos raices reales")
    elif dis < 0:
        print("la funcion f tiene dos raices complejas conjugadas")
    else:
        print("la funcion f tiene una unica raiz") 
    if b>0:
         x2 = (-b+dis**0.5)/(2*a)
         x1 = c/(a*x2)
    else:
         x2 = (-b-dis**0.5)/(2*a)
         x1 = c/(a*x2)
    return x1, x2