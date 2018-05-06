'''

8.Crea una función que reciba un número e imprime si es primo o no.

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Números primos

def primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
        print "no es primo"
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            print "no es primo"
    print "Es primo"    #de lo contrario devuelve Verdadero


#bloque principal
numero = int(raw_input("introduce numero para saber si es primo : "))
primo(numero)


