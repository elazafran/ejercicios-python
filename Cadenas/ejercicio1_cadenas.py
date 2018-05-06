'''

1.Escribir un programa que reciba una cadena de unos y ceros (es decir, un número en representación binaria)
y devuelva el valor decimal correspondiente.


'''
'''
cadena = raw_input("introduzca una cadena : ")
resultado=0

for i in cadena[::-1]:
    pritn i
    #resultado=resultado + cadena[int(i)]*(2**int(i))

print resultado
'''

cad1=raw_input("Numero binario:")		

cont=0
decimal=0
for num in cad1[::-1]:
     if str(num)=="1":
         decimal=decimal+(2**cont)
     cont=cont+1
print decimal
