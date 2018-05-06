'''
6. Escriba un programa que pida al usuario dos números enteros,
y luego entregue la suma de todos los números que están entre ellos.
Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20. Se comprobara que  num1> num2
si no se cumple se volverá a pedir  num2

Ejemplo 1 al 4= 2+3 correcto
Ejemplo 10 al 4 no correcto y se pedirá otro número en lugar del 4
'''

resultado =0

n1 = int (raw_input("indroduzca primer numero entero : "))
if n1<0:
    n1 = int (raw_input("Valor no valido, indroduzca primer numero entero : "))
else:    
    n2 = int (raw_input("indroduzca segundo numero entero : "))
    while n2<n1:
        print "el numero anterior %d" % (n1)
        n2 = int (raw_input("valor no valido, indroduzca segundo numero entero :"))

tN1=n1+1
tN2=n2
for i in range(tN1,tN2):
    resultado=resultado+i
    print "resultado %d " %(resultado)
    
