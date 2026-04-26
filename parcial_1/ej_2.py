import matplotlib.pyplot as plt
from ej_1 import serie_seno

# Variables iniciales
segmento = [0, 6.4]
res = 0.01
cant_pto = int((segmento[1]-segmento[0])/res)
print(cant_pto)

# Definición de dominio
dom = []
for i in range(cant_pto + 1):
    dom.append(i*((segmento[1]-segmento[0])/cant_pto)+segmento[0]) # para calcular la pendiente y  poder terminos negativvos en el dom
#el calculo de la recta sirve para poder tener terminos negativos en el dom, y generalizar los valores del segmento

# Obtener imagen
img = []

for i in range(cant_pto + 1):
    img.append(serie_seno(dom[i]))

# Graficar
plt.plot(dom, img)
plt.grid(True, linestyle='--', color='gray', alpha=0.7)
plt.show()
print(dom)