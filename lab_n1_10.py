import random

def sonreciprocos(x,y):
    if x*y==1:
        return True
    else:
        return False


for _ in range(100):
    x = 1 + random.random()
    y = 1 / x
    if not sonreciprocos(x,y):
        print(x)

#vemos que x*y si son iguala uno es True, en caso contrario es False.
#Luego toamoas 100 nros, random y definimos x como estos nros. e y la divison y pedimos que si no son reciprocos nos imprima solo x
#EN RESUMEN: genera 100 números aleatorios x entre 1 y 2, luego calcula y = 1/x. Comprueba si son recíprocos con sonreciprocos, luego imprime x si la comprobación falla. Y por ultimo el posible "fallo" se debe a errores de precisión de los números decimales.