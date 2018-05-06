'''

9.Crear una función que reciba una cadena y
retorno su longitud sin usar la función len

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Números primos

def longuitud(cadena):
    resultado=0
    for i in cadena:
        resultado+=1
    return resultado

#bloque principal
cadena = raw_input("introduce numero para saber si es primo : ")
print longuitud(cadena)


