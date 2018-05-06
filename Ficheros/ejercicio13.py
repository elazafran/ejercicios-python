#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

13. Función que recibe una lista de enteros y devuelve otra lista con aquello que son pares y >= 113(return)

'''
lista=[1,22,130,55,144,135,77]
def enteros(lista):
   resultado=[]
   for i in lista:
       if i%2==0 and i>=113:
           resultado.append(i)
   return resultado

print (enteros(lista))
