#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

4.Crea un diccionario donde se pedirán por teclado el
    código de un producto, nombre, y stock del producto la clave será el código.

Se pide realizar un menú con las siguientes opciones, cada uno de los apartados se hará con funciones
1.Pedir datos
2.Listar todos los productos
3.Listar los productos que sean iguales que uno pedido por teclado
4.Salir

'''


productos = {}
productos["15"] = [6103, 7540]


def pedirDatos():
    codigo= input("código de un producto: ")
    nombre= input("nombre de un producto: ")
    stock=input("stock de un producto: ")
    productos[codigo]=[nombre,stock]

def listarProductos():
    print (productos)


def listarIguales():
    buscar = input("Listar los productos que sean iguales que uno pedido por teclado: ")
    if buscar in productos:
        print (productos[buscar])


while True:
    opcion = int(input("selecione opcion:"
                           + "\n1.Pedir datos"
                           + "\n2.Listar todos los productos"
                           + "\n3.Listar los productos que sean iguales que uno pedido por teclado"
                           + "\n4.Salir\nIntroduzca : "))
    if opcion == 1:
        pedirDatos()
    if opcion == 2:
        listarProductos()
    if opcion == 3:
        listarIguales()
    if opcion == 4:
        break

