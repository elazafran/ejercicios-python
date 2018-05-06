import tkinter as tk

import pylab as pl
import numpy as np



def Create_plot(c,b,lInferior,lSuperior):
    #dibujamos
    pl.plot(c,b)
    #definimos el limites
    pl.ylim(lInferior, lSuperior)
    #pl.ylim(lInferior, lSuperior)
    #leyenda de la x
    pl.xlabel("x(radianes)")
    # Mostrar resultado en pantalla
    pl.show()

    
def mostrarConsulta():
    lInferior = float(limiteInferior.get())
    lSuperior = float(limiteSuperior.get())
    origen =  float(origenGrafica.get())
    x = np.linspace(origen,2*np.pi,150)
    ycos = np.sin(x)
    print(lInferior)
    print(lSuperior)
    
    Create_plot(x,ycos,lInferior,lSuperior)

ventana = tk.Tk()
#dimensiones
ventana.geometry("500x400+100+100")
#ventanas
ventana.title("Gráfica de un seno")

#colocamos los elementos por posicion absoluta
tk.Label(ventana, text="Limite superior").place(x=150, y=20)
limiteSuperior = tk.StringVar()
tk.Entry(ventana, textvariable=limiteSuperior, width=30).place(x=150, y=50)


tk.Label(ventana, text="Limite inferior").place(x=150, y=80)
limiteInferior = tk.StringVar()
tk.Entry(ventana, textvariable=limiteInferior, width=30).place(x=150, y=110)

tk.Label(ventana, text="Origen de la grafica").place(x=150, y=150)
origenGrafica = tk.StringVar()
tk.Entry(ventana, textvariable=origenGrafica, width=30).place(x=150, y=180)

tk.Button(ventana, text="mostrar grafica",  command = mostrarConsulta).place(x=200, y=340)

#lanzamos el loop
ventana.mainloop()

