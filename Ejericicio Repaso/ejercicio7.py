'''
7.Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.
'''
letra = raw_input("Introduzca una letra: ")

lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","Z"]

hay = lista.count(letra)

if hay==0:
    print "es minuscula"
else:
    print "es mayuscula"


'''

Opcion optima

'''

letra = raw_input("letra")
if letra>="A" and letra<="Z":
    print " mayuscula "
else
    print " minuscula "
