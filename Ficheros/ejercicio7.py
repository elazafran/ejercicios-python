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

lista = []


def annadirElementos():
    elemento = input("introduzca elemento a lista: \n")
    lista.append(elemento)


def listLista():
    print(lista)


def annadirElementosPorPosicion():
    elemento = input("introduzca elemento a lista: \n")
    posicion = int(input("introduzca posicion que desea: \n"))
    lista.insert(posicion, elemento)


def borrarElemento():
    elemento = int(input("introduzca elemento a lista a borrar, introduzca posicion: \n"))
    lista.pop(elemento)


def ordenar():
    lista.sort()
    print(lista)


def totalElementos():
    print(len(lista))


def recorrerInversa():
    for i in reversed(lista):
        print(i)


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
        annadirElementos()
    if opcion == 2:
        listLista()
    if opcion == 3:
        annadirElementosPorPosicion()
    if opcion == 4:
        borrarElemento()
    if opcion == 5:
        ordenar()
    if opcion == 6:
        totalElementos()
    if opcion == 7:
        recorrerInversa()
    if opcion == 0:
        break
