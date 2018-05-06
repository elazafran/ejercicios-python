'''

Crea una función que reciba 2 números y devuelva el resto de la división
del primer número dividido entre el segundo. Imprime el resultado.


'''

def esmayor(numero1,numero2):
    if numero2 == 0:
        print "el número1",numero1," es igual que", numero2
    else:
        print "el resto es",numero1%numero2
        

    
    
#bloque principal
numero1 = int(raw_input("introduce numero "))
numero2 = int(raw_input("introduce numero "))   

esmayor(numero1,numero2)
