'''
1.Escribir un programa que reciba una cadena de unos y ceros
(es decir, un número en representación binaria)
y devuelva el valor decimal correspondiente.

'''

numeroBinario=raw_input("Escriba un numero en binario: ")
numeroDecimal=0
exp=0


for i in numeroBinario[::-1]:
   
   numeroDecimal=numeroDecimal+(int(i)*(2**exp))
   exp=exp+1

  
print numeroDecimal
