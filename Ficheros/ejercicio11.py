#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

11.Anadir una línea con los números 1, 2, 3 ... 10 al fichero datos.txt

'''

def addLine():
    contador=0
    file = open("datos.txt","a")
    numeros=""
    for i in range(0,10):
        numeros=str(numeros+str(i))
    file.write(str(numeros))
addLine()



