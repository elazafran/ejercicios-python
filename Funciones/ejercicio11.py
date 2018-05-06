'''

11.Crea una función multiplicar y otra suma para sumar y multiplicar
los elementos de una lista predefinida.
Ambas funciones imprimirán el resultado

lista = [1,3,5,7,9]

la multiplicacion es 945
la suma es 25
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-


lista = [1,3,5,7,9]


def sumar(lista):
    resultado=0
    for i in lista:
        resultado+=i
    print "la suma es",resultado

def multiplicar(lista):
    resultado=1
    for i in lista:
        resultado*=i
    print "la multiplicacion es",resultado
    
#bloque principal
multiplicar(lista)
sumar(lista)




