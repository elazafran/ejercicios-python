#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
9.Imprime por pantalla el numero de líneas del fichero
'''

def readFile():
    file = open("datos.txt","r")
    print(len(file.readlines()))
    file.close()

readFile()

