'''

Crear un programa que lea por teclado una cadena, y muestre la siguiente información:
Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
Imprima la cadena en un sentido y en sentido inverso.

'''

cadena = raw_input("introduzca una cadena : ")

print ("")
print ("los dos primeros caracteres ")
print cadena[:2]


print ("")
print ("los tres últimos caracteres ")
print cadena[-3:]


print ("")
print ("Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca ")
print cadena[::2]

print ("")
print ("Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh")
print cadena[::-1]

print ("")
print ("Imprima la cadena en un sentido y en sentido inverso")
print cadena+cadena[::-1]


