# Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
 

# Guardamos los centimetros
centimetros = input("Introduce la centimetros a convertir: ")


# Definimos funcion para hacer la conversion 
def convertir():
        
        resultado= centimetros*2.54
        return format(resultado,".2f")

resultado_final=convertir()

""" Imprime los datos """
print("Centimetros:", centimetros )

print("El valor en pulgadas es : ", resultado_final + "\"")

