'''
6. Escribe un programa que, al recibir como dato un número entero N, obtenga el resultado de
la siguiente serie 

 ** exponente

'''
resultado = 0
entrada1 = int(raw_input("introduzca número: "))


for i in range (1,entrada1+1):
    print (i**i)
    if i%2==0:
        resultado = resultado - (i**i)
    else:
        resultado = resultado + (i**i)

print "ha terminado %f"%resultado
