def sonortogonales(vector_1, vector_2):
    n=len(vector_1)

    producto_interno = 0
    for i in range(n):
        producto_interno=producto_interno+vector_1[i]*vector_2[i]
    
    if producto_interno==0:
        return True
    else:
        return False
    
#Ahora ejecutaremos las instrucciones pedidas por el ejercicio:
x=[1,1.102407412658109]
y=[-1,1/x[1]]
if not sonortogonales(x,y):
    print("algo salio mal...")
else:print("vectores ortogonales correctamente")
