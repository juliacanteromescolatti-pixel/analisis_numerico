"""10. Integral con tolerancia
Calcular: la inttegral de cero a uno de sen(x)dx usando Simpson compuesto.
Aumentar automáticamente N hasta que: ∣In - In/2∣<10**(−6)"""

import numpy as np

#Definición de la función
def f(x):
    return x * np.sin(x)

a = 0.0
b = 1.0
tolerancia = 1e-6

#Función de Simpson Compuesto
def simpson_compuesto(fun, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    res_parcial = 0 
    
    for j in range(len(x)):
        if j == 0 or j == len(x) - 1:
            res_parcial += fun(x[j])
        elif j % 2 == 0:
            res_parcial += 2 * fun(x[j])
        else:
            res_parcial += 4 * fun(x[j])
            
    res_final = (h / 3) * res_parcial
    return res_final

#Bucle de aumento automático de N (Control de Tolerancia)
# Empezamos con N = 2 (el mínimo para Simpson)
N_anterior = 2
I_anterior = simpson_compuesto(f, a, b, N_anterior)

# Duplicamos N para empezar a comparar
N_actual = 4

# Bandera para controlar el bucle
condicion_cumplida = False

while not condicion_cumplida:
    # Calculamos la integral con el N actual
    I_actual = simpson_compuesto(f, a, b, N_actual)
    
    # Calculamos el error estimado (diferencia en valor absoluto)
    diferencia = abs(I_actual - I_anterior)

    
    # Verificamos el criterio de parada
    if diferencia < tolerancia:
        condicion_cumplida = True
    else:
        # Si no cumple, el actual pasa a ser el anterior para la próxima vuelta...
        I_anterior = I_actual
        N_anterior = N_actual
        # ...y duplicamos N
        N_actual = N_actual * 2

print("CONVERGENCIA LOGRADA")
print("El valor de N final requerido es =", N_actual)
print("La aproximación final de la integral es =", I_actual)


# La integral de x*sin(x) por partes es: sin(x) - x*cos(x)
valor_exacto = (np.sin(1.0) - 1.0 * np.cos(1.0)) - (np.sin(0.0) - 0.0 * np.cos(0.0))
print("Valor analítico exacto real =",valor_exacto)
print("Error absoluto real final =", abs(valor_exacto - I_actual))

"""El Inicio empeizo con False
Por eso le avisás a Python que la condición todavía no se cumplió.
El Bucle (while not condicion_cumplida):"Mientras no se haya cumplido la condición, 
seguí repitiendo lo que está acá adentro". 
Como al principio es False, el while se activa y empieza a calcular.
El Control: Adentro del bucle, el programa calcula la integral y mide la diferencia.
El Cambio: Si la diferencia todavía es grande, la condición sigue siendo False 
y el bucle da otra vuelta (duplica $N$ y vuelve a calcular).
En el momento exacto en que la diferencia se vuelve más chica que 10**(-6), 
el código ejecuta la línea: condicion_cumplida = True"""