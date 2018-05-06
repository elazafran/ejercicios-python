'''

7.Crea una función que reciba un número, calcule su factorial, e imprímelo.


'''

def factorial(numero):

    result = 1
    for i in xrange(2, numero + 1):
        result *= i
    print result


    
    
#bloque principal
numero = int(raw_input("introduce numero para calcular factorial"))
factorial(numero)


