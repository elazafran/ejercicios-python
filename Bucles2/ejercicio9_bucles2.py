'''
9.Un analista financiero lleva un registro del precio del dólar día a día,
y desea saber cuál fue la mayor de las alzas en el precio diario a lo largo de ese período.
Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio del dólar para cada uno de los n días.
El programa debe entregar como salida cuál fue la mayor de las alzas de un día para el otro.

'''
nDias = int (raw_input("Numero de días"))
nDias= nDias+1

'''
for i in range (1,nDias):
    resultado=dia2-dia1
    dia1 = float(raw_input("valor del barril"))
    print "Resuladot %f" %resultado


        n = int(raw_input("Cuantos dias? "))

'''
diferencia = 0
dia_anterior = 0

for i in range(1,nDias):
   dia = float(raw_input("Dia "+str(i)+": "))
   if dia - dia_anterior > diferencia and i>1: 
       diferencia = dia - dia_anterior
   
   dia_anterior = dia         

print "La mayor diferencia fue de %f euros" % diferencia
