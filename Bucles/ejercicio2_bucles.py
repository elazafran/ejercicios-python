'''
2. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y
la media de todos los números introducidos. Usar While
'''
numero = 0
suma = 0
contador = 1
numero = int (raw_input("Introduzca numero : "))
while numero!=0 :
    suma = suma + numero
    contador= contador+1
    media = suma/(contador-1)
    numero = int (raw_input("Introduzca numero : "))


print("El total es : " , suma, " el contador es ", contador, "la media es:" , media)
print("la media es %f")%media

#%d y lo coje como entero
