# Factorial de 6 act5 p1
def fac(n = 6):
	if(n == 0):
		resu=1
	elif(n > 0):
		resu = 1
		for i in range (1,n+1):
			resu= resu*i
	else:
		print("factorial no esta defndo para el numero que ingreso")
	return resu		    
