#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

2.Crear una lista de paciente se introducirá datos hasta que digamos que no queremos insertar más datos
en la lista y finalmente guardar la lista en un fichero.

Datos que se pedirán del paciente nombre. El fichero se llamara paciente.txt y atributo “a”
Menú con las siguiente opciones
1.Crear fichero
2.Leer fichero
3. Salir

'''
lista=[]

while True:
        paciente = raw_input("introduzca nombre de pacientes o no si desea salir: \n")
        if paciente=="no":
                break
        else:
                lista.append(paciente)
                print lista
	
def crearFichero():
        nombreFichero="paciente.txt"
        p = open(nombreFichero,"a")
        for l in lista:
                print l
                p.write(l+"\n")
        p.close()
	
        

def leerFichero(nombreFichero):
	
	p=open(nombreFichero,"r")
	print p.read()
	p.close()

while True:
        opcion=int(raw_input("selecione opcion:"
                         +"\n1.crear fichero"
                         +"\n2.Leer fichero"
                         +"\n3.Salir\nIntroduzca : "))
        if opcion==1:
                crearFichero()
        if opcion==2:
                nombreFichero="paciente.txt"
                leerFichero(nombreFichero)
        if opcion==3:
                break
        
