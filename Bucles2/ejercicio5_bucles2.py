'''
5.Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

'''
resultado=0
minutosTramo = int (raw_input("indroduzca los minutos del tramo : "))
resultado=resultado+minutosTramo
while minutosTramo!=0:
    minutosTramo=  int (raw_input("indroduzca los minutos del tramo : "))
    resultado=resultado+minutosTramo

horas = float(resultado/60)
minutos = float(resultado%60)
print horas,"horas",minutos,"minutos"
