"""6. Escribir un programa que pida dos numeros reales e imprima en la pantalla el mayor de
ellos. El programa debe indicar si los numeros son iguales."""

# Definimos la función que solo se encarga de la lógica matemática
def comparar(x, y):
    if x < y:
        print("El mayor es el segundo número:", y)
    elif x == y:
        print("Ambos números son iguales")
    else:
        print("El mayor es el primer número:", x)

# 1. Pedimos los números FUERA de la función usando float() para aceptar reales
numero1 = float(input("Ingrese un primer número real (ej. 3.14): "))
numero2 = float(input("Ingrese un segundo número real (ej. 5.5): "))

# 2. Llamamos a la función pasándole los números que ingresó el usuario
comparar(numero1, numero2)