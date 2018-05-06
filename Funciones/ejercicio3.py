'''

Crea una función que reciba 2 números, devuelve el mayor e imprímelo.


'''

def esmayor(numero1,numero2):
    if numero1 == numero2:
        return "el número1",numero1," es igual que", numero2
    else:
        if numero1>numero2:
            return "el número1",numero1," es mayor que", numero2
        else :
            return "el número1",numero1," es mayor que", numero2
        

    
    
#bloque principal
numero1 = int(raw_input("introduce numero"))
numero2 = int(raw_input("introduce numero"))   

print esmayor(numero1,numero2)
