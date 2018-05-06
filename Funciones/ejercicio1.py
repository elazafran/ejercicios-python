'''

Crea una función que reciba un número e imprima si es par o impar.

'''

def esparoimpar(numero):
    if numero%2==0:
        print "el número es par"
    else :
        print " el número no es par"
    

def entradaDatos():
    numero = int(raw_input("introduce numero"))
    esparoimpar(numero)
    
    
#bloque principal
entradaDatos()
    
