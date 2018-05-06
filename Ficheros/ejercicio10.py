#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
10.El numero de enteros que hay en la primera línea del fichero.
'''

def readFile():
    contador=0
    file = open("datos.txt","r")
    for i in file:
        for k in i:
            if k!=" ":
                contador = contador+1
        break
    print(contador-1)
readFile()



