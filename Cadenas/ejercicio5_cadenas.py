'''

Crear un programa que lea por teclado una cadena y un carácter,
y reemplace todos los dígitos en la cadena por el carácter.
Ej: su clave es: 1540 y X debería devolver su clave es: XXXX 

'''

cadena=raw_input("introduzca una clave:")
caracter=raw_input("introduzca un caracter:")

clave=""
for i in cadena:
    clave=clave+caracter
    
print clave
print "----"

