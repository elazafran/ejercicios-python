'''

12.Crear y cargar una lista con 5 enteros por teclado.
Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

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
print "posicion en el array (empieza en 0)",listaEnteros.index(mayor)
