'''
2.Escribir un programa python que dado una palabra diga si es un palíndromo.
Un palídromo Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás.
Ejemplo: reconocer

'''


palindromo = raw_input("Introduzca numero en palindromo")

inverso = palindromo[::-1]

if (palindromo==inverso):
    print "Es un palindromo"
else:
    print "No es un palindromo"
    


