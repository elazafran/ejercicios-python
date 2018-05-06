'''
3.Introduce números por teclado  y guárdalo en una lista,
el proceso finaliza cuando metamos un número negativo.
Muestra el máximo de los números guardado en la lista,
muestra los números pares.

'''
lista=[]
max=0
while(True):
    numero = int(raw_input("Introduzca numeros,el proceso finaliza cuando metamos un número negativo "))
    if numero>max:
        max=numero
    
    if numero <0 :
        print "salimos "
        print lista
        break;
    else:
        lista.append(numero)

print "el numero maximo introducido es: ",max


