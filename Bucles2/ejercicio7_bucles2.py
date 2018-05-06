'''
7. Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
Ingrese num: 10

1 2 4 8 16 32 64 128 256 512 1024

'''

resultado = 0
potencia = int (raw_input("Ingrese num de potencia"))
rangofinal = potencia+1
for i in range(0,rangofinal):
    potenciacalulada=(2**i)
    resultado = resultado+potenciacalulada
    print "resultado de 2 elevado %d , da como resultado %d" %(i,potenciacalulada)
    
'''print "Resultado final %d" %(resultado)'''
