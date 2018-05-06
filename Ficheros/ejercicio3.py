#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

3.Crear un fichero llamado alumno.txt en el que se almacenara el nombre ,
apellido y curso del alumno y finalmente se mostrará toda
la información que contiene el fichero alumno.txt. Sin usar funciones

'''
nombreFichero="alumno.txt"
p = open(nombreFichero,"a")
        
lista=[]
entrada=""

while True:
        if entrada !="no":
                entrada = raw_input("introduzca nombre: ")
                p.write(entrada+" - ")
                entrada = raw_input("introduzca apellido: ")
                p.write(entrada+" - ")
                entrada = raw_input("introduzca curso: ")
                p.write("\n")
        else:
                break
    
p.close()
	
        
