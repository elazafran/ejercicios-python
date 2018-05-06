
"""

Escriba un programa que pida dos números enteros y que calcule la división,
indicando si la división es exacta o no.
 
"""

# Guardamos los datos del usuario
n1 = int(raw_input("numero 1 \n"))
n2 = int(raw_input("numero 2 \n"))

def calcular():
        
        resultado = n1/n2
        resto = n1%n2
        if (resto==0):
                print("la division es exacta")
        else:
                print("la division es inexacta")
        return format(resto)

resultado_final = calcular()
print (resultado_final)



