#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1.Crea una función que pida el nombre de un fichero y su atributo( “añadir”) 
el fichero contendrá los 10 primeros números , 
también se creara una función para leer fichero realizar un menú con las siguientes opciones

	1.Crear fichero
	2.Leer fichero
	3.salir

'''

	
def crearFichero():
	nombreFichero=input("Introduzca nombre de fichero: ")
	p = open(nombreFichero,"a")
	p.write("1,2,3,4,5,6,7,8,9,10")
	print (p)
	p.close()

def leerFichero(nombreFichero):
	p=open(nombreFichero,"r")
    print(p.read())
    p.close()

while True:
        opcion=int(input("selecione opcion:"
                         +"\n1.crear fichero"
                         +"\n2.Leer fichero"
                         +"\n3.Salir\nIntroduzca : "))
        if opcion==1:
                crearFichero()
        if opcion==2:
                nombreFichero=input("Introduzca nombre de fichero: ")
                leerFichero(nombreFichero)
        if opcion==3:
                break
        
#crearFichero(nombreFichero)
#leerFichero(nombreFichero)


