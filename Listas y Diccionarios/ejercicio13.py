'''
13. Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.

1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.

'''
'''
articulos = {}
articulos["raton"] = [25]
articulos["pendrive"] = [30]
articulos["ssd"] = [89]
articulos["teclado"] = [10]
articulos["pantalla"] = [150.0]


for articulo, precio in articulos.items():
   print articulo, ":", precio
print "Precios mayores a 100\n"
'''
articulos = {}

for i in range(2):
   articulo_nombre= raw_input("introduzca nombre producto")
   articulo_precio= int (raw_input("introduzca precio producto"))
   articulos[articulo_nombre]=articulo_precio
   print "\n"
   

for nombre in articulos:
   if articulos[nombre]>100:
      print nombre



     
