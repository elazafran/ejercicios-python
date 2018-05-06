#  Cn = C * (1 + x/100) ^ n
#Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular. Hallar cuanto vale Cn. El resultado vendra dado con dos decimales
#el exponente se pone ** en python

# Guardamos los datos del usuario
capital_inicial = float(raw_input("Cantidad de euros: "))
tasa_interes = float(raw_input("Introduce la tasa de interes: "))
numero_anios = float(raw_input("Introduce los años "))


# Definimos funcion
def cantidad_a_pagar():
        
        Cn = capital_inicial * (1 + tasa_interes/100) **numero_anios 
        return format(Cn,".2f")



resultado=cantidad_a_pagar()

""" Imprime los datos """
print("capital_inicial:", capital_inicial)
print("tasa_interes:", tasa_interes)
print("numero_anios:", numero_anios)

print("La cantidad a pagar :  ", resultado)

