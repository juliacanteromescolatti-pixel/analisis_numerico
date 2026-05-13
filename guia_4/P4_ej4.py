"""Italia fue el paìs màs afectado por el Coronavirus, comenzando con 14 casos desde el 22 de febrero
de 2020 y con una cantidad de infectados que creciò exponencialmente por màs de un mes. Obtener
los datos almacenados en el archivo covid italia.csv y realizar un ajuste exponencial de la forma
y(x) = aebx. Realizar un gràfico que contenga los datos y su ajuste."""

import numpy as np
import matplotlib.pyplot as plt

# Ajuste exponencial de la forma: y = a*e^(bx)

# LEER LOS DATOS:
datos = np.loadtxt("/home/kmom/analisis_numerico/guia_4/archivos necesarios/covid_italia.csv",delimiter=",",skiprows=1)

# Primera columna = x (dias)
x = datos[:,0]

# Segunda columna = y (infectados)
y = datos[:,1]

# IDEA DEL AJUSTE EXPONENCIAL:
# Queremos ajustar: y = a*e^(bx)
# Pero polyfit SOLO ajusta rectas: y = mx + b
#Entonces transformamos el modelo exponencial en uno lineal usando logaritmos.
#Aplicamos logaritmo natural: ln(y) = ln(a*e^(bx))
#Propiedades: ln(y) = ln(a) + ln(e^(bx)) y como: ln(e^(bx)) = bx queda: ln(y) = bx + ln(a)
#Esto YA es una recta: Y = bX + c donde: Y = ln(y), X = x, pendiente = b y ordenada = ln(a)
#Entonces hacemos un ajuste lineal sobre: x y ln(y)

# TRANSFORMAMOS LOS DATOS
# Calcula ln(y)
Y = np.log(y)

# AJUSTE LINEAL:
# polyfit(x, Y, 1) busca la recta: Y = mx + p
# Devuelve: m = pendiente y p = ordenada
# En nuestro caso: pendiente = b; ordenada = ln(a)

b, ln_a = np.polyfit(x, Y, 1)


# RECUPERAR a:

# Tenemos: ln(a) = ln_a
# Entonces: a = e^(ln_a)
# np.exp calcula exponencial
a = np.exp(ln_a)

# Mostrar coeficientes
print("a =", a)
print("b =", b)

# CURVA AJUSTADA
# Generamos MUCHOS puntos entre el menor y mayor x, para que la curva salga suave
xi = np.linspace(min(x), max(x), 200)

# Evaluamos la funcion:
#y = a*e^(bx)
#En todos los puntos xi, O sea: yi = a*e^(b*xi)
yi = a * np.exp(b * xi)


# GRAFICAR
# Datos originales
plt.plot(x, y, "o")
# Curva ajustada
plt.plot(xi, yi)
plt.grid(True, linestyle='--', color='gray')
plt.title("Act 4 - Ajuste exponencial COVID Italia")
plt.show()