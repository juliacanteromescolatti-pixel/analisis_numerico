from ej_1 import serie_seno
from P2_ej1 import rbisec

I1 = [1,4.5]
I2 = [4.5,5.5]
err = 1e-5
mit = 100

#Primera raiz
hx,hf = rbisec(serie_seno,I1,err,mit)
print(hx,hf)

#Segunda raiz
hx,hf = rbisec(serie_seno,I2,err,mit)
print(hx,hf)

