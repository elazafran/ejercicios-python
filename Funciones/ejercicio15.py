'''

15.Definir un histograma que tome una lista de números enteros
e imprima el histograma en pantalla

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-


lista = [1,3,5,7,9]


def histograma(lista):
    
    resultado=""
    for i in lista:
        print i
        for j in range(1,i+1):
            resultado+="*"
        print resultado   

#bloque principal


histograma(lista)



