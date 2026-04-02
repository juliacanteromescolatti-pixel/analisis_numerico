"""
escribir dos funciones para la resulucion de ecuaciones de segundo grado
del tipo ax**2+bx+c
una sera mala (usando la forma tradicional)
y la otra buena (creada de manera eficiente para evitar la perdida de digitos)
"""
def buena():
    a=int(input("introduzca un numero para ser el termino acompañando a x cuadrado: "))
    b=int(input("introduzca un numero para ser el termino acompañando de x: "))
    c=int(input("introduzca un numero para ser el termino independiente: "))
    dis=((b)**2-4*a*c)**0.5
    if dis > 0:
        print("la funcion f tiene dos raices reales")
    elif dis < 0:
        print("la funcion f tiene dos raices complejas conjugadas")
    else:
        print("la funcion f tiene una unica raiz") 
    x1 = (-b+dis)/(2*a)
    x2 = (-b-dis)/(2*a)
    return (x2)
