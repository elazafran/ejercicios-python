'''
9. Escribir una función que reciba una lista de elementos e indique si se encuentran ordenados de menor a mayor o no.
Se acabara cuando introduzcamos un numero negativo. Se puede usar la función sort
'''

lista=[1,2,7,3,4,5]

#listaOrdenada=[1,2,3,4,5,6,7,8,9,10]

comprobar=[]
comprobar = lista[:]
comprobar.sort()

    
if lista == comprobar:
    print "está ordenada"
else:
    print "NO está ordenada"


print lista
print comprobar

'''
num=int(raw_input("Número:"))
lista=[]

while num>0:
    lista.append(num)
    num=int(raw_input("Número:"))
lista2=lista[:]
lista.sort()

if lista==lista2:
    print "Ordenada"
else:
    print "No ordenada"
'''
