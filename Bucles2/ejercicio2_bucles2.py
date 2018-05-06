'''
1.Un jugador debe lanzar dos dados numerados de 1 a 6, y su puntaje es la suma de los valores obtenidos.
Un puntaje dado puede ser obtenido con varias combinaciones posibles. Por ejemplo, el puntaje 4 se logra con las siguientes tres combinaciones: 1+3, 2+2 y 3+1.
Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado la cantidad de combinaciones de dados con las que se puede obtener ese puntaje.

'''
numeros_positivos =0
numeros_negativos =0

entrada=1
while entrada!=0:
    entrada = int (raw_input("indrouzca un numero entero : "))
    if(entrada>0):
        numeros_positivos=numeros_positivos+1
    if(entrada<0):
        numeros_negativos=numeros_negativos+1

print "numeros_positivos : ",
for i in range(0,numeros_positivos):
    print "*",
print ""
print "numeros_negativos : ",
for i in range(0,numeros_negativos):
    print "*",
