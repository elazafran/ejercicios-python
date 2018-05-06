'''
5.A partir de dos listas de enteros, 'numeros1' y 'numeros2',
crea una lista que contiene aquellos valores de la primera que
también están en la segunda e imprímela por pantalla.

Es decir, calcula la intersección de ambas listas. 
'''
numeros1=[1,2,3,4,5,6]
numeros2=[1,6]
interseccion=[]

for i in numeros2:
    for j in numeros1:
        #print "%d el numero de j"%j
        if i==j:
            interseccion.append(j)
        else:
            print "no coinciden"
    

print "resultado:",interseccion
