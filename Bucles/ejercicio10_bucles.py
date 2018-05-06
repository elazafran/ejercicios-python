'''

10. Crea una aplicación que pida un número y calcule su factorial (El factorial de un
número es el producto de todos los enteros entre 1 y el propio número y se
representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
1x2x3x4x5=120), hacedlo con un for
'''
 
"""

Ejemplo del factorial de 5 seria:
	5 * 4 * 3 * 2 * 1  = 120
"""
 
def factorial(x,n):
	"""
	Función recursiva que calcula el factorial
	Tiene que recibir:
		x=>El ultimo valor calculado
		n=>El numero a multiplicar
	"""
	if(n>0):
		# Se va llamando a ella misma mientras el valor sea superior a 0
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x
 
try:
	numero = int(raw_input("inserta un numero "))
 
	# Ejecutamos la función recusiva para el calculo
	calculo=factorial(1,numero)
	print "El factorial de %s es %s" % (numero,calculo)
except:
	print "\nTiene que ser un valor numerico"
