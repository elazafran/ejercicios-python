'''
10. Un número primo es un número natural que sólo es divisible por 1 y por sí mismo.
Escriba un programa que reciba como entrada un número natural, e indique si es primo o compuesto.
Los números que tienen más de un divisor se llaman números compuestos. El número 1 no es ni primo ni compuesto.
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
