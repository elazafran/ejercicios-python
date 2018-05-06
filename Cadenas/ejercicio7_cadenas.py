'''


7.Escribir una función que reciba una cadena que contiene un número entero y devuelva una cadena
con el número y las separaciones de miles.
Por ejemplo, si recibe 1234567890, debe devolver 1.234.567.890.

'''

def devolver(numero):
    numeroDevolver=numero;
    i = numeroDevolver.index('.') # Se busca la posicion del punto decimal
    while i>3:
        i=i-3
        numeroDevolver=numeroDevolver[:i]+','+numeroDevolver[i:]
        
    return numeroDevolver

numero=int(raw_input("introduzca una cadena:"))

print devolver('%.2f'%(float(numero),))
print "----"

