'''
8.Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
Ingrese su fecha de nacimiento.
Dia: 14
Mes: 6
Anno: 1948
Usted tiene 62 annos
Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.
Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):
Además deberá indicar si ya ha pasado su cumple o no e imprimir la fecha actual

'''
from time import localtime
import time;

t = localtime()

print "ingrese su fecha de nacimeinto"

dia = int(raw_input("introduzca dia "))
mes = int(raw_input("introduzca mes "))
annio = int(raw_input("introduzca annio "))


if t.tm_mon>mes:
    print "ya ha pasaod tu cumple"
else:
    print"todavia no ha sido tu cumple"

print "tiene",t.tm_year-annio,"annios"


fecha_actual = time.asctime( time.localtime(time.time()) )
print "Fecha actual :", fecha_actual
