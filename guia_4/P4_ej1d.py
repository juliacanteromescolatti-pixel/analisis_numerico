"""
(d) Encontrar el valor de m tal que la recta y = m(x-1/2)ajuste lo mejor posible los
datos del ıtem anterior en el sentido de cuadrados mínimo
"""

"""
IMPORTANTE
m = sum_yi(xi-0.5)/(sum_(xi)-0.5)**2
"""

import numpy as np
import matplotlib.pyplot as plt

print("Si despejamos de la formula de minimos cuadrados el m que mejor obtenemos es: ")
x = np.linspace(0, 10, 20)
y_real = (3/4)*x-0.5
y = y_real + np.random.randn(len(x))

z = x - 0.5
m = np.sum((y*z)/np.sum(z**2))

y_ajuste = m*(x - 0.5)
print("m = ", m)




# Graficar
plt.plot(x,y, "o", label="ajuste")
plt.plot(x, y_real, label="recta real")
plt.legend()
plt.title("Act 1-(d)")
plt.grid(True, linestyle='--', color='gray')
plt.show()

