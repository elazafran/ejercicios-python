#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

12.La suma de todos los números impares del documento datos.txt

'''

p = open("datos.txt", "r")
s = p.read()
lista = [int(x) for x in s.split()]
resultado = 0
for i in lista:
    if i % 2 != 0:
        resultado = resultado + i
print(resultado)
