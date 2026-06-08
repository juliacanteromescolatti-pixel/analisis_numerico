"""Ajuste polinomial Generar 50 puntos de: f(x)=cos(x) en [0,2π].
Ajustar polinomios de grado: [0,1,2,3,4,5[]
Calcular la suma de residuos para cada uno. Determinar cuál ajusta mejor."""
import numpy as np
import matplotlib.pyplot as plt

#Generación de los 50 puntos según el enunciado
# Creamos 50 puntos equiespaciados en el eje X desde 0 hasta 2*pi
x = np.linspace(0, 2 * np.pi, 50)

# Calculamos sus valores reales en el eje Y aplicando el Coseno
y = np.cos(x)

# Definimos la lista con los grados de los polinomios que nos pide evaluar
grados = [0, 1, 2, 3, 4, 5]

# Variables para guardar cuál es el que mejor resultado nos da
mejor_grado = -1
menor_residuo = float('inf') # Empezamos con un número infinito para comparar

for g in grados:
    # 'polyfit' calcula los coeficientes del polinomio de grado 'g'
    coeficientes = np.polyfit(x, y, g)
    
    # 'polyval' evalúa el polinomio en nuestros mismos puntos x
    # Esto nos da las alturas aproximadas que genera la curva
    y_aproximada = np.polyval(coeficientes, x)
    
    # Calculamos la SUMA DE RESIDUOS:
    # Restamos el valor real menos el aproximado, lo elevamos al cuadrado
    # para quitar los signos negativos, y sumamos todos los errores.
    residuo = np.sum((y - y_aproximada) ** 2)
    
    print("g =", residuo)
    
    # Si este residuo es menor al que teníamos guardado, actualizamos el mejor
    if residuo < menor_residuo:
        menor_residuo = residuo
        mejor_grado = g
        
    # Dibujamos la curva de este grado de forma suave en el gráfico
    x_suave = np.linspace(0, 2 * np.pi, 200)
    y_suave = np.polyval(coeficientes, x_suave)
    plt.plot(x_suave, y_suave, label=f'Polin. Grado {g}')

print(f"RESULTADO: El polinomio que MEJOR ajusta es el de GRADO {mejor_grado}.")

#Configuración visual del gráfico
plt.title('Ajuste Polinomial para f(x) = cos(x)')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

#El -1 es para decir: "Todavía no hay ningún grado ganador".
#El infinito es para decir: "Cualquier error que aparezca primero va a ser el nuevo récord a vencer".