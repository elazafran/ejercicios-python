'''

2.Escribir un programa python que dado una palabra diga si es un palíndromo. Un palídromo Un palíndromo es una palabra,
número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer
'''

cad1=raw_input("introduzca cadena:")		

if cad1==cad1[::-1]:
    print "es un palindromo"
else:
    print "no es un palindromo"
