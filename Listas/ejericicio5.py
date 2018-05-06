'''
5. Escribe un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
Por último, el programa tiene que escribir la lista.

'''


numeroPalabras = 0
lista=[]
numeroPalabras = int(raw_input("numero de palabras a crear"))

for i in range(0,numeroPalabras):
    cadena = raw_input("diga palabra")
    lista.append(cadena)    

print lista
