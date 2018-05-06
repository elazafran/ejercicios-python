'''
4. Escribe un programa que pida por teclado palabras y la inserte en una lista
se dejara de introducir datos cuando se introduzca un espacio en blanco.

A continuación se pedirá una palabra y calcule cuantas palabras hay iguales en la lista
que la palabra introducida

'''

lista=[]
max=0
while(True):
    palabras = raw_input("Introduzca palabras,el proceso finaliza cuando metamos un número negativo ")
    
    if palabras==" ":
        print "salimos "
        print lista
        break;
    else:
        lista.append(palabras)

buscar = raw_input("Introduzca palabra a buscar")
print lista.count(buscar)

    

