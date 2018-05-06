# Hallar el área y el perímetro de una circunferencia. El radio se pedirá por teclado. La solución tendrá dos decimales
 
from math import pi
 
 
# Defining Funtions
def circle_perimeter(radio):
	""" formula: perimetro = 2 * pi * radio """
	radio = float(radio)# We convert the input in floating
	perimeter = 2 * pi * radio
 
	return format(perimeter, ".1f")# We give format to one floating point
 
def cicle_area(radio):
	""" formula: area = pi * radio ** 2 """
	radio = float(radio)# We convert the input in floating, again
	area = pi * radio ** 2 # We can too uses parenthesis, but this will work
 
	return format(area, ".1f")# We give format to one floating point
 
 
''' Ejecutar las funciones  '''
# Perimetro
radio = input("Introduce el radio del circulo: ")
result_per = circle_perimeter(radio)
 
# Area
result_ar = cicle_area(radio)
 
 
""" Imprime """
print("Perimetro:", result_per + "cm2")
print("Área:", result_ar + "cm2")
