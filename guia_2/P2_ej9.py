"""Dada la ecuacion, lo que haremso sera restar E de ambos lados, y asi quedar una ecuacion con laincognita D
(cuadratica) igualada a cero, para asi aplicar el metodo de newton.
Pues los datos de E y V los tenemos, solo nos falta calcular D"""
""""Busco encontrar el diámetro del molino para que genere 500 W con viento de 6.667 m/s.
Eso es la raíz que busco con el metodo de Newton.
Por eso palnteo un posible diametro inicial tq al aplicar Newton temine de encontrar el adecuado que satisfaga
f = 0.01328 * D**2 * V**3 - 500"""
from P2_ej3 import rnewton

# velocidad en m/s
V = 24 / 3.6

# función + derivada
def fun(D):
    f = 0.01328 * D**2 * V**3 - 500
    df = 2 * 0.01328 * D * V**3
    return f, df

# D0=valor inicial para empezar a iterar. Es tu primer intento del diámetro.
D0 = 10

# ejecutar Newton
raiz = rnewton(fun, D0, 1e-6, 100)

print("Diámetro:", raiz)
"""EN EL RESULTADO EL PRIMER [] SERAN LOS D INICIALES UQE SE REFIERE A LOS VALORES INCIALES,
 Y EL SEGUNDO[] SON LOS VALORES DE LA FUNCION ES ESOS PUNTOS."""