'''

13.Definir una función llamada comparar que comparara dos cadenas y retornara
True si tiene algún valor igual que la otra cadena y
False si no tine ninguno igual

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-


lista = [1,3,5,7,9]


def comparar(cadena1,cadena2):
    for i in cadena1:
        for j in cadena2:
            if i==j:
                return True
    return False

#bloque principal
cadena1 = raw_input("introduzca cadena1: ")
cadena2 = raw_input("introduzca cadena2: ")

print comparar(cadena1,cadena2)



