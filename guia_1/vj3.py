#act 3 OVERFLOW P1
import math
def suma_al (s=2):
	contador=0
	while math.isinf (s) == False:
		s=s*2
		contador=contador+1
	   # print(contador)
	return s, contador
#UNDERFLOW P2
import math
def suma_al1 (s=2):
	dcontador=0
	while s != 0:
		s=s/2
		contador=contador+1
    return s, contador
