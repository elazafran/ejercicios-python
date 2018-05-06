#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

6. Realizar una calculadora aritmética con funciones. Crear el siguiente menú
1.Suma
2.Resta
3.Multiplica
4.División
5.Salir

'''



def suma():
    numero1 = int(input("introduzca numero 1: \n"))
    numero2 = int(input("introduzca numero 2: \n"))
    print (numero1 + numero2)


def resta():
    numero1 = int(input("introduzca numero 1: \n"))
    numero2 = int(input("introduzca numero 2: \n"))
    print (numero1 - numero2)


def multiplica():
    numero1 = int(input("introduzca numero 1: \n"))
    numero2 = int(input("introduzca numero 2: \n"))
    print (numero1 * numero2)


def divsion():
    numero1 = int(input("introduzca numero 1: \n"))
    numero2 = int(input("introduzca numero 2: \n"))
    if numero2==0:
        print("valor no valido introduzca otro valor : \n")
        numero2 = int(input("introduzca numero 2: \n"))
    print (numero1/numero2)
    pass


while True:
    opcion = int(input("selecione opcion:"
                           + "\n1.suma"
                           + "\n2.resta"
                           + "\n3.multiplica"
                           + "\n4.división"
                           + "\n5.Salir\nIntroduzca : "))
    if opcion == 1:
        suma()
    if opcion == 2:
        resta()
    if opcion == 3:
        multiplica()
    if opcion == 4:
        divsion()
    if opcion == 5:
        break