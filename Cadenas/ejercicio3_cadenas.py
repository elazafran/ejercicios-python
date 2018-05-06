'''

3.Modifica el programa para que compruebe si una frase es palíndroma.
Ejemplo: Yo hago yoga hoy


'''

frase=raw_input("introduzca una frase:")		
temp = frase.replace(' ', '')

if temp==temp[::-1]:
    print('la frase es un palindromo')
else :
    print('la frase NO es un palindromo')
    
print "----"

