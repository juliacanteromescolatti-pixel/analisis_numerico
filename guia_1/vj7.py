#act 7 p1
# "n" y "x" son input, con n entero  y r real
def pot(n,x):
	#n = int(input(" pone un numero para ser el exponente de nuestra potencia, porfi: "))
	#x= float(input("pone un numero para ser la base de nuestra potencia, porfi: "))
	if(n == 0):
		x=1
	elif(n > 0):
		s = x
		for i in range (1,n):
			x= x*s
	else:
		print("la putencia no esta defndo para el numero que usted ingreso")
	return x	    

def nue(x):
    for n in range(1,6):
        print(pot(n,x))
