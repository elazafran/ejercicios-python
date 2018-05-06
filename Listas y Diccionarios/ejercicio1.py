'''
8.Crear un programa que lea por teclado una cadena y un carácter,
y reemplace todos los dígitos en la cadena por el carácter.
Ej: su clave es: 1540 y X debería devolver su clave es: XXXX 

'''

cadena = raw_input("Introduzca una cadena: ")
caracter = raw_input("Introduzca un caracter: ")

conversor = len(cadena)
resultado = caracter
lista = []
lista = cadena

print lista
'''

for i in cadena:
      
    if i>="0" and i<="9":
        print "numero"
    else:    
        resultado=resultado+caracter
    
print resultado

for i in range(0,9+1):
    cadena = cadena.replace(str(i),caracter)

print
print cadena


'''  

resultado =2;
while resultado<=2048
    print resultado;
    resultado = resultado*2
