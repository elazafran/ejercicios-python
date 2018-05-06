'''

12.Crea una función llamada
palíndromo que imprima por pantalla si una cadena es palíndroma o no

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-


lista = [1,3,5,7,9]


def palindromo(cadena):
    
    if cadena== cadena[::-1]:
        print "es un palindromo"
    else:
        print "no es un palindromo"
    
    
#bloque principal
cadena = raw_input("introuzca cadena: ")

palindromo(cadena)



