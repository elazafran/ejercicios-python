'''
4.Lee una cadena de texto del usuario y para cada letra
indica si es una vocal o una consonante 
Es decir hola
H :consonante
O:vocal
L:consonante
A:vocal
'''



'''
cadena = raw_input("Introduzca cadena : \n")
for i in cadena.lower():
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        print "%s es una vocal"%i.upper()
    else:    
        print "%s es una consonante"%i.upper()
'''

vocales ="aeiou"
palabra = raw_input("Introduzca cadena : \n")
for letra in palabra:
    print letra
    if letra.lower() in vocales:
        print "es una volca"
    else:
        print "es una consonante"
