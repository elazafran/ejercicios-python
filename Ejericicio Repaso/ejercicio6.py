'''
6. Un número primo es un número natural que sólo es divisible por 1 y por sí mismo.
Escriba un programa que reciba como entrada un número natural, e indique si es primo o compuesto.
Los números que tienen más de un divisor se llaman números compuestos. El número 1 no es ni primo ni compuesto

'''
numero = int(raw_input("Introduzca es primo o compuesto "))

divisible = 0

if numero==1 and numero==0:
    print "salimos, no es ni primo ni compuesto"

else:
    for i in range(2,numero+1):
        if numero%i==0:
            divisible=divisible+1
        
if divisible<2:
    print "es primo"
else:
    print "no es primo, es compuesto"

