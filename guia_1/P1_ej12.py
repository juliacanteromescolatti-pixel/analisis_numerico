"""Tengo que definir esta funcion con "x" e "y" dos vectores 
y que devuelva True si son ortogonales"""
def sonortogonales(x,y):
    producto_punto= x[0]*y[0] + x[1]*y[1]  
    """estoy tomando el elemneto cero de lalista y 
    el elemneto uno de la lista, para hcer el producto vectorial de x1 con y1 y x2 con y2"""
#Veamso que pd es cero
    if producto_punto ==0:
        return True
    else:
        return False
    
#Ahora ejecutaremos las instrucciones pedidas por el ejercicio:
x=[1,1.102407412658109]
y=[-1,1/x[1]]
if not sonortogonales(x,y):
    print("algo salio mal...")
else:print("vectores ortogonales correctamente")

#Resumen:

"""Mi función calcula correctamente si dos vectores son ortogonales, 
los vectores que elegi cumplen la condición de ortogonalidad (producto punto = 0) 
por eso se imprime "vectores ortogonales correctamente"; 
si elijieramos otro "x" y otro "y" apareceria que algo salio mal."""