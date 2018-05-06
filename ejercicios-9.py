
"""

Introduce un año por teclado y comprueba si es bisiesto o no para establecer si un año dado es bisiesto: (% modulo)

es bisiesto si es divisible entre cuatro
 si es divisible entre 100 no es bisiesto
 si es divisible entre 400 es bisiesto
 
"""

# Guardamos los datos del usuario

anio=int(raw_input("ingresa año\n"))
if(anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0):
 print("El año "+str(anio)+" Si es bisiesto ")
else:
 print("El año "+str(anio)+" No es bisiesto ")




