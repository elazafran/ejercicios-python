'''
8. Escribe un programa que pida por teclado palabras y la inserte en una lista
se dejara de introducir datos cuando se introduzca un espacio en blanco.

A continuación se pedirá una palabra y calcule cuantas palabras hay iguales en la lista que la palabra introducida

'''
listaPalabras=[]
palabras = raw_input("introduzca palabra")

while palabras!=" ":
    listaPalabras.append(palabras)    
    palabras = raw_input("introduzca palabra")
    

print "ha introducido un espacio en blanco"

palabraAbuscar = raw_input("introduzca palabra a buscar")
print listaPalabras.count(palabraAbuscar)
