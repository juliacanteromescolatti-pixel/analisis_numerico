from ej_4 import rsteffensen
from ej_1 import serie_seno

x0 = 3
x1 = 6
x2 = 4.45 #se va muy lejos pues en el deniminador tengo la resta de dos cosas parecidas (en 4.67 converge a la raiz 4.96 y en 4.4 esta la otra convergencia)
err = 1e-5
mit = 100

#Primera raiz
hx,hf = rsteffensen(serie_seno, x0, err, mit)
print(hx,hf)
print(len(hx),len(hf))

#Segunda raiz
hx,hf = rsteffensen(serie_seno, x1, err, mit)
print(hx,hf)
print(len(hx),len(hf))

#Tercera raiz
hx,hf = rsteffensen(serie_seno, x2, err, mit)
print(hx)
print(len(hx),len(hf))