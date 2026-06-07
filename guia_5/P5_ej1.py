# ACT 1
#Funciones de prueba
def fun1(x):
	y = x
	return y
    
def fun2(x):
	y = x**3
	return y
	
def intecomp(fun, a, b, n, regla:str):   #fa y fb: Calcula la altura de la función en los dos extremos absolutos del intervalo (a y b).
	fa=fun(a)
	fb=fun(b)
	if regla == "simpson":
		h = (b-a)/(2*n)
		sx0 = fa+fb
		sx1 = 0 # suma de terminos impares
		sx2 = 0 # suma de terminos pares
		x = a
		for j in range (1, 2*n): #suma terminos pares
			x = x + h
			if j%2 == 0:
				sx2 = sx2 + fun(x)	
			else:   #suma terminos imapres
				sx1 = sx1 + fun(x)
			sx = (sx0+2*sx2+4*sx1)*(h/3) #aplica regla de simpson
		return sx
	elif regla == "trapecio":
		h = (b-a)/n
		sx0 = fa + fb
		sx1 = 0
		x = a
		for j in range (1, n):
			x = x + h
			sx1 = sx1 + fun(x)
		sx = (sx0+2*sx1)*(h/2)
		return sx
	elif regla == "pm":
		h = (b-a)/(2 + n)
		sx1 = 0 # suma de terminos pares
		x = a + h
		for j in range (0, n//2):  #ponemos // para referirnos a que n es un numero entero
			x = x + h
			if j%2 == 0:
				sx1 = sx1 + fun(x)
			else:
				None 
		sx = sx1*2*h
		return sx
