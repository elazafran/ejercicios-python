'''

13.Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años) .
(Se deberá crear dos lista una para el nombre y otro para la edad)

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
