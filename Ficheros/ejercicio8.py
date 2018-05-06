#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

8.Imprime por pantalla la longitud de la primera línea
del fichero datos

'''


def crearFichero():
    nombreFichero = input("Introduzca nombre de fichero: ")
    p = open(nombreFichero, "a")
    p.write("Hola esto es un mensaje")
    print(p)
    p.close()


def leerFichero():
    p = open("javi.txt", "r")
    for i in p:
        print(len(i))
        break



leerFichero()