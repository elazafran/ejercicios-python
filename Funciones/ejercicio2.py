'''

Modifica la función anterior para que en vez de imprimirlo lo devuelva.


'''

def esparoimpar(numero):
    if numero%2==0:
        return "el número es par"
    else :
        return " el número no es par"
    

def entradaDatos():
    numero = int(raw_input("introduce numero"))
    resultado = esparoimpar(numero)

    print resultado
    
    
#bloque principal
entradaDatos()
    
