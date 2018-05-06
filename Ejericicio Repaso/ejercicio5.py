'''
5.Escribe un programa que al recibir un numero positivo  N, calcula el resultado de la siguiente serie
1+(1/2)+(1/3)+(1/4)……1/N
Si el usuario introduce un numero negativo escribirá numero incorrecto y se acabara el programa

'''
numero = int(raw_input("Introduzca nuermo,el proceso finaliza cuando metamos un número negativo "))
resultado = float(1)
if numero<=0:
    print "salimos "
    
else:
    for i in range (1,numero+1):
        resultado = resultado + (1/float(i))
        
print resultado

