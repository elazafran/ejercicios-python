'''

14.Definir una función que tome un entero y un carácter e imprima
el carácter muliplicado por el entero es decir
Ingrese numero=3
Ingrese carácter: x
XXX

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-


lista = [1,3,5,7,9]


def convertir(numero,caracter):
    
    resultado =""
    for i in range (numero):
        resultado+=caracter
    print resultado    

#bloque principal
numero = int(raw_input("introduzca numero: "))
caracter = raw_input("introduzca caracter: ")

convertir(numero,caracter)



