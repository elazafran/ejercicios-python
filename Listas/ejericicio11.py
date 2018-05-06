'''

11.Crear y cargar una lista con 5 enteros.
Implementar un algoritmo que identifique el mayor valor de la lista. E imprime la lista entera

'''

listaEnteros = []

mayor = 0

for i in range(0,5):

    enteros =  raw_input("introduzca enteros : ")
    listaEnteros.append(enteros)
    for i in listaEnteros:
        
        if i >=mayor:
            mayor=i


print listaEnteros
print mayor
