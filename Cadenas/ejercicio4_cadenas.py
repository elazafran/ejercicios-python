'''

4 Crear un programa que lea por teclado una cadena y un carácter,
y reemplace todos los espacios por el carácter.
Ej: mi archivo de texto.txt y _ debería devolver mi_archivo_de_texto.txt 


'''

frase=raw_input("introduzca una frase:")		
temp = frase.replace(' ', '_')

print temp
print "----"

