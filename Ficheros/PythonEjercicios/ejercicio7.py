#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

7.Crea una lista mediante funciones con el siguiente menú
1.Añadir elementos
2 Listar la lista
3 añadir elementos en una posición pedida por teclado
4.Borrar elemento de una lista pedido por teclado
5.Ordenar la lista
6.Total de elementos de la lista
7.Recorrer la lista inversa
0.Salir

'''

lista=[]

def addElements():
    elemento= int(input("introduzca elemento a lista: \n"))
    lista.append(elemento)

def listLista():
    print (lista)


def addElementsPosition():
    elemento = int(input("introduzca elemento a lista: \n"))
    posicion = int(input("introduzca posicion que desea: \n"))
    lista.insert(posicion,elemento)


def deleteElement():
    elemento = int(input("introduzca elemento a lista a borrar: \n"))
    lista.pop(elemento)


def divsion():
    numero1 = int(input("introduzca numero 1: \n"))
    numero2 = int(input("introduzca numero 2: \n"))
    if numero2==0:
        print("valor no valido introduzca otro valor : \n")
        numero2 = int(input("introduzca numero 2: \n"))
    print (numero1/numero2)
    pass


def ordenar():
    lista.sort();


while True:
    opcion = int(input("selecione opcion:"
                           + "\n1.Añadir elementos"
                           + "\n2.Listar la lista"
                           + "\n3.Añadir elementos en una posición pedida por teclado"
                           + "\n4.Borrar elemento de una lista pedido por teclado"
                           + "\n5.Ordenar la lista"
                           + "\n6.Total de elementos de la lista"
                           + "\n7.Recorrer la lista inversa"
                           + "\n0.Salir\nIntroduzca : "))
    if opcion == 1:
        addElements()
    if opcion == 2:
        listLista()
    if opcion == 3:
        addElementsPosition()
    if opcion == 4:
        divsion()
    if opcion == 5:
        ordenar()
    if opcion == 6:
        divsion()
    if opcion == 7:
        divsion()
    if opcion == 0:
        break