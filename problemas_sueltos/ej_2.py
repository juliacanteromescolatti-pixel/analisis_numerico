"""Act 2: Overflow controlado.
Escribí un programa que encuentre el mayor número de la forma 2**n
representable en Python antes de overflow. Devolvé también el valor de n."""
import math

x = 1.0   # empezamos en 2^0
n = 0
#No quiero que sea infinito pues sino seria Overflow
while not math.isinf(x):
    ultimo = x
    n_ultimo = n
    
    x = x * 2
    n = n + 1

print("Mayor potencia representable:")
print("2^", n_ultimo, "=", ultimo)