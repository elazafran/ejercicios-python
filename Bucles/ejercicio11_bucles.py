'''

11. Programa que pida diez numero y determine cuantos son positivos y cuantos son
negativos(for)

'''
 


numerosPositivios = 0
numerosNegativos  = 0
for i in range(1,11):
    numero = int(raw_input("inserta un numero "))
    if (numero >0):            
        numerosPositivios = numerosPositivios+1
    if numero<0:
        numerosNegativos =  numerosNegativos +1
    
print "Hay %s numeros positivos y %s numeros negativos" % (numerosPositivios,numerosNegativos)

