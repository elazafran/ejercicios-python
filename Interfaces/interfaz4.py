#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tkinter import *

# listas grafica 1
listaX = []
listaY = []
listaXY = []

# listas grafica 2
listaPX=[]
listaPY=[]
listaPXY=[]

listaNX = []
listaNY = []
listaNXY = []

def mostrarGrafica1():

    # recogemos los datos
    listaX.append(float(editext1.get()))
    listaX.append(float(editext2.get()))
    listaX.append(float(editext3.get()))
    listaX.append(float(editext4.get()))
    listaX.append(float(editext5.get()))

    # relleanmos los datos
    for i in range(len(listaX)):
        listaY.append((i ** 2) + 1)


    for i in range(0, 5):
        x = listaX[i]
        y = listaY[i]
        listaXY.append([x, y])

    # estilos de la grafica y datos.
    plt.plot(listaX, listaY, marker='x', linestyle=':', color='y', label="y=x^2+1")

    # etiquetas
    plt.ylabel('Eje de Ordenada')
    plt.xlabel('Eje de Abscisa')
    plt.title('Ecuacion')

    # localizacion de la etiquetas
    plt.legend(loc="upper left")
    print(listaXY)

    # mostramos la grafica
    plt.show()

def mostrarGrafica2():


    # rellenamos valores
    valorX1 = float(editext1.get())
    valorY1 = valorX1 ** 2 + 1
    listaPX.append(valorX1)
    listaPY.append(valorY1)
    listaPXY.append([valorX1, valorY1])

    valorX2 = float(editext2.get())
    valorY2 = valorX2 ** 2 + 1
    listaPX.append(valorX2)
    listaPY.append(valorY2)
    listaPXY.append([valorX2, valorY2])

    valorX3 = float(editext3.get())
    valorY3 = valorX3 ** 2 + 1
    listaPX.append(valorX3)
    listaPY.append(valorY3)
    listaPXY.append([valorX3, valorY3])

    valorX4 = float(editext4.get())
    valorY4 = valorX4 ** 2 + 1
    listaPX.append(valorX4)
    listaPY.append(valorY4)
    listaPXY.append([valorX4, valorY4])

    valorX5 = float(editext5.get())
    valorY5 = valorX5 ** 2 + 1
    listaPX.append(valorX5)
    listaPY.append(valorY5)
    listaPXY.append([valorX5, valorY5])



    # rellenamos valores
    valorX6 = float(editext6.get())
    valorY6 = valorX6 ** 2 + 1
    listaNX.append(valorX6)
    listaNY.append(valorY6)
    listaNXY.append([valorX6, valorY6])

    valorX7 = float(editext7.get())
    valorY7 = valorX7 ** 2 + 1
    listaNX.append(valorX7)
    listaNY.append(valorY7)
    listaNXY.append([valorX7, valorY7])

    valorX8 = float(editext8.get())
    valorY8 = valorX8 ** 2 + 1
    listaNX.append(valorX8)
    listaNY.append(valorY8)
    listaNXY.append([valorX8, valorY8])

    valorX9 = float(editext9.get())
    valorY9 = valorX9 ** 2 + 1
    listaNX.append(valorX9)
    listaNY.append(valorY9)
    listaNXY.append([valorX9, valorY9])

    valorX10 = float(editext10.get())
    valorY10 = valorX10 ** 2 + 1
    listaNX.append(valorX10)
    listaNY.append(valorY10)
    listaNXY.append([valorX10, valorY10])

    #dividimos las graficas
    plt.subplot(1, 2, 2)
    plt.plot((listaPX), (listaPY), marker='X', color='g', linestyle=':', label='y=x^2+1')
    plt.legend(loc="upper left")

    plt.subplot(1, 2, 1)
    plt.plot((listaNX), (listaNY), marker='.', color='r', linestyle=':', label='y=x^2+1')
    plt.legend(loc="upper left")

    #mostramos valores por consola
    print()
    print("valores de la rama 1", listaPXY)
    print("valores de la rama 2", listaNXY)

    # guardamos la grafica en formato PNG
    plt.show()

master = Tk()
master.title("Ejercicio 4")

#inicializamos elementos de entrada
editext1 = Entry(master)
editext2 = Entry(master)
editext3 = Entry(master)
editext4 = Entry(master)
editext5 = Entry(master)
editext6 = Entry(master)
editext7 = Entry(master)
editext8 = Entry(master)
editext9 = Entry(master)
editext10 = Entry(master)

#colocamos elementos
Label(master, text="Apartado A").grid(row=0, column=1,pady=10)
Label(master, text="Valor 1").grid(row=1, column=1)
Label(master, text="Valor 2").grid(row=2, column=1)
Label(master, text="Valor 3").grid(row=3, column=1)
Label(master, text="Valor 4").grid(row=4, column=1)
Label(master, text="Valor 5").grid(row=5, column=1)
Label(master, text="").grid(row=6, column=1)
Label(master, text="Apartado B").grid(row=7, column=1,pady=10)
Label(master, text="Valor 1").grid(row=8, column=1)
Label(master, text="Valor 2").grid(row=9, column=1)
Label(master, text="Valor 3").grid(row=10, column=1)
Label(master, text="Valor 4").grid(row=11, column=1)
Label(master, text="Valor 5").grid(row=12, column=1)

editext1.grid(row=1, column=2)
editext2.grid(row=2, column=2)
editext3.grid(row=3, column=2)
editext4.grid(row=4, column=2)
editext5.grid(row=5, column=2)
editext6.grid(row=8, column=2)
editext7.grid(row=9, column=2)
editext8.grid(row=10, column=2)
editext9.grid(row=11, column=2)
editext10.grid(row=12, column=2)

var = IntVar()
#colocamos botones y label de acciones
Label(master, text="Seleccione el tipo de gráfica").grid(row=14, column=2,pady=20)
radioButton1 = Radiobutton(master, text="Apartado A", variable=var, value=1, command=mostrarGrafica1).grid(row=15, column=1,pady=10)
radioButton2 = Radiobutton(master, text="Apartado B", variable=var, value=2, command=mostrarGrafica2).grid(row=15, column=2,pady=10)
master.geometry("500x400+100+100")
master.mainloop( )