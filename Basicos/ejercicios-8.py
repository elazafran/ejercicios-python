
#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.


# Guardamos los datos del usuario


num = raw_input("Introduce un número: ")
num = int(num)

""" Imprime los datos """

if num == 0:
    print ("Este número es par.")
elif num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")




