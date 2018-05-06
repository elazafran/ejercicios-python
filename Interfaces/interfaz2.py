#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tkinter import *

nombres = ["Navegador 1","Navegador 2","Navegador 3","Navegador 4","Navegador 5"]
valores = []

def mostrarGrafica():

    # Añaadimos cinco elementos a ambas listas preguntando
    # al usuario
    valores.append(float(editText1.get()))
    valores.append(float(editText2.get()))
    valores.append(float(editText3.get()))
    valores.append(float(editText4.get()))
    valores.append(float(editText5.get()))

    # Le pasamos los valores y etiquetas
    plt.pie(valores, labels=nombres, autopct='%1.1f%%')

    # Mostramos la leyenda
    plt.legend()
    plt.show()


master = Tk()
#titulo
master.title("Porcentaje de uso de navegadores")
#tamaño ventana
master.geometry("500x400+100+100")

#inicializamos elementos de entrada
editText1 = Entry(master)
editText2 = Entry(master)
editText3 = Entry(master)
editText4 = Entry(master)
editText5 = Entry(master)

#colocamos los elementos
Label(master, text="").grid(row=0)
Label(master, text="Navegador 1",height=2).grid(row=1,column=1)
Label(master, text="Navegador 2",height=2).grid(row=2,column=1)
Label(master, text="Navegador 3",height=2).grid(row=3,column=1)
Label(master, text="Navegador 4",height=2).grid(row=4,column=1)
Label(master, text="Navegador 5",height=2).grid(row=5,column=1)

editText1.grid(row=1, column=2)
editText2.grid(row=2, column=2)
editText3.grid(row=3, column=2)
editText4.grid(row=4, column=2)
editText5.grid(row=5, column=2)


#botones de accion
Button(master, text='Mostrar', command=mostrarGrafica).grid(row=6, column=2, sticky=W, pady=4)

#iniciamos loop
master.mainloop( )