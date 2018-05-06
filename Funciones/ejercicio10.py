'''

10.Escribe una función que tome un carácter y retorne True si es una vocal
y False cuando no sea una vocal

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Números primos
lista = {"a","e","i","o","u"}

def retorno(caracter):
    if caracter in lista:
        return True
    else:
        return False

#bloque principal
caracter = raw_input("introduce caracter : ")
print retorno(caracter)


