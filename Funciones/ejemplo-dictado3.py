'''
Crea una funcion que reciba un numero e imprima si es par o inpar

'''
def pedirNumero():
    numero = int(raw_input("Ingresa valor : "))
    resultadoFinal = esPar(numero)    

def esPar(numero):
    if numero%2==0:
        resultado = True
        #resultado = "es par"
        print "es par"
    else:
        resultado = False
        #resultado = "no es par"
        print "no es par"
    return resultado
    

#bloque principal

pedirNumero()

#print "el número es(true) o no es par (false): ",resultadoFinal

    
