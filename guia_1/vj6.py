# act6

def may(x,y):
	if (x<y):
		print(y)
	elif (x == y):
		print("los numeros que pusiste son iguales hermane")
	else:
		print(x)
	return may

x=float(input("ingrese un primer numero: "))
y=float(input("ingrese un segundo numero: "))

may(x,y)
