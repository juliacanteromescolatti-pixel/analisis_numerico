#JULIA CANTERO MESCOLATTI
#Act 1:
#INCISO A
def fun(k):
    termino = 1/ ((2**k)*k)
    return termino

def serie_sn(k):
    resultado = 0
    terminos = []
    for i in range(k): #porque quiero que mi sumatoria empiece desde k = 1 y sume los terminos hasta obtener mi resultado deseado
        terminos.append(fun(i+1)) #obtengo el termino i, y lo voy agregando a la lista
        resultado = resultado + terminos[i] #para obtrener el resultado, hago el rsultado inicial mas el primer termino, y asi sucecivamente
    return resultado
#Probemos algunos valores para ver si mi sumatoria funciona
serie_sn(8)
print(serie_sn(8))
#Empiezo con k = 1, pero no lo pongo dentro del codigo pues sino siemnpre valdria que k = 1, pues no puedo dividir por cero
k = 1

#INCISO B
#Como me pide un bucle para encontrar el menor k tq la suma se estanque en un punto flotante, es decir que el proceso finalice en Sk = Sk+1, usare un bucle while
#Usamos while pues no sabemos cuantas iteraciones serán necesarias, solo sabemos la condicion de parada que es que Sk == Sk+1

while serie_sn(k)!= serie_sn(k+1):
    k = k + 1
    print("No son iguales")
if serie_sn(k) == serie_sn(k+1):
    print("Son iguales")  #Frena pues Sk == Sk+1

#INCICO C:
print(f"El valor de k es {k}, que es la cantidad de iteraciones necesarias para el estancamineto.")
print(f"El valor de la funcion en k es {serie_sn(k)}, es decir que este es el valor donde la serie converge.")