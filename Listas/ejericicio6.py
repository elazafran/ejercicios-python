'''
6. Dada una lista de números enteros (guarda la lista en una variable) y un entero k, escribir un programa que:
Cree tres listas , una con los menores, otra con los mayores y otra con los iguales a k.
Crea otra lista lista con aquellos que son múltiplos de k.

Ejemplo
lista=[1,2,3,4,5,6,7] y k=2 estas dos variables la definís no hace falta meterla por teclado
lista=[2,4,6,1,3,4,5,7,8]
  k=4

'''
k=2
#lista=[1,2,3,4,5,6,7]
lista=[1,1,1,4,5,6,7]
listaMenores=[]
listaIguales=[]
listaMayores=[]

for i in lista:
    if i < k :
        listaMenores.append(i)
    elif i == k :
        listaIguales.append(i)
    else:
        listaMayores.append(i)

print "listaMenores " ,listaMenores
print "listaIguales " ,listaIguales
print "listaMayores " ,listaMayores
