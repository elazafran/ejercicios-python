'''
5. Escribe un programa que al recibir un numero positivo N, calcula el resultado de la siguiente
serie
1+(1/2)+(1/3)+(1/4)……1/N
Si el usuario introduce un número negativo escribirá número incorrecto y se acabara el
programa

'''
resultado = 0
entrada1 = int(raw_input("introduzca número: "))


for i in range (1,entrada1+1):
    print 1/float(i) 
    resultado = resultado + (1/float(i))


print "ha terminado %f"%resultado
