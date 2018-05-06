
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
#el exponente se pone ** en python

'''
T(°C) = (T(°F) - 32) / 1.8
Example
Convert 68 degrees Fahrenheit to degrees Celsius:
T(°C) = (68°F - 32) × 5/9 = 20 °C

'''

# Guardamos los datos del usuario
fahrenheit  = float(raw_input("Grados Fahrenheit a convertir: "))


# Definimos funcion
def convertir():
        
        resultado = (fahrenheit - 32) / 1.8
        return format(resultado,".2f")



resultado=convertir()

""" Imprime los datos """
print("Los grados celcius son :", resultado + "C")

