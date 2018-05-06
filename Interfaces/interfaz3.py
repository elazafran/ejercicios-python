#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

#lista de meses
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre")

def grafica():

    posicion_y = np.arange(len(meses))
    #recogemos valores
    unidades = (editText1.get(), editText2.get(), editText3.get(), editText4.get(), editText5.get(), editText6.get(), editText7.get(), editText8.get(), editText9.get(), editText10.get(), editText11.get(), editText12.get())

    #pintamos grafica
    plt.bar(meses,unidades,color='blue',align='center')
    ax=plt.axes()

    #Etiquetas de los ejes
    plt.xlabel('Cantidad de litros')
    plt.title("Lluvias del año 2018")
    plt.show()

def graficaSectores():

    # recogemos valores
    unidades = (editText1.get(), editText2.get(), editText3.get(), editText4.get(), editText5.get(), editText6.get(),editText7.get(), editText8.get(), editText9.get(), editText10.get(),editText11.get(), editText12.get())
    plt.pie(unidades, labels=meses, autopct='%1.1f%%', shadow=True)

    # mostramos leyenda
    plt.legend()
    #mostramos titulo
    plt.title("Lluvias del año 2018")
    plt.show()

master = Tk()
#Titulo
master.title("Lluvias del año 2018")

#inicializamos las variables
editText1 = Entry(master)
editText2 = Entry(master)
editText3 = Entry(master)
editText4 = Entry(master)
editText5 = Entry(master)
editText6 = Entry(master)
editText7 = Entry(master)
editText8 = Entry(master)
editText9 = Entry(master)
editText10 = Entry(master)
editText11 = Entry(master)
editText12 = Entry(master)


#colocamos los elementos
Label(master, text="Enero").grid(row=0, column=2)
Label(master, text="Febrero").grid(row=1, column=2)
Label(master, text="Marzo").grid(row=2, column=2)
Label(master, text="Abril").grid(row=3, column=2)
Label(master, text="Mayo").grid(row=4, column=2)
Label(master, text="Junio").grid(row=5, column=2)
Label(master, text="Julio").grid(row=6, column=2)
Label(master, text="Agosto").grid(row=7, column=2)
Label(master, text="Septiembre").grid(row=8, column=2)
Label(master, text="Octubre").grid(row=9, column=2)
Label(master, text="Noviembre").grid(row=10, column=2)
Label(master, text="Diciembre").grid(row=11, column=2)

#colocamos los elementos de entrada
editText1.grid(row=0, column=3)
editText2.grid(row=1, column=3)
editText3.grid(row=2, column=3)
editText4.grid(row=3, column=3)
editText5.grid(row=4, column=3)
editText6.grid(row=5, column=3)
editText7.grid(row=6, column=3)
editText8.grid(row=7, column=3)
editText9.grid(row=8, column=3)
editText10.grid(row=9, column=3)
editText11.grid(row=10, column=3)
editText12.grid(row=11, column=3)


#posicionamos los botones
Button(master, text='Grafica 1', command=grafica).grid(row=12, column=2, sticky=W, pady=20)
Button(master, text='Grafica 2', command=graficaSectores).grid(row=12, column=4, sticky=W, pady=20)

#iniciamos loop
master.mainloop( )