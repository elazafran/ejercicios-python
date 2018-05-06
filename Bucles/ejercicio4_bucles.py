'''
4. Escribir un programa que imprima todos los números pares entre dos números que se
le pidan al usuario.(for)

'''

entrada1 = int(raw_input("introduzca numero 1: "))
entrada2 = int(raw_input("introduzca numero 2: "))

for i in range (entrada1,entrada2+1):
    
    if i%2==0:
        print i
    
print "ha terminado porque ha metido un espacio"
