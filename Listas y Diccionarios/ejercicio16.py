'''
16) Confeccionar un programa que permita cargar un código de producto como clave en un diccionario.
Guardar para dicha clave el nombre del producto, cantidad en stock.

Implementar las siguientes actividades:
1) Introducir 5 elementos.
2) Listado completo de productos.
3) Consulta de un producto por su clave(código), mostrar el nombre, stock.
En caso de que no exista el código se pondrá no existe


'''


diccionario = {}

for i in range(5):
   clave= raw_input("introduzca codigo de producto")
   valor= raw_input("introduzca su nombre")
   valor2= raw_input("cantidad")
   
   if(clave =="no" or valor=="no"):
      break
   else:
      if clave not in diccionario.keys():
         diccionario[clave]=valor
         print "añadimos"
      else:   
         print "NO añadimos"
      
print diccionario


clave= raw_input("introduzca numero de documento a buscar")

if clave in diccionario.keys():
   print diccionario[clave]
   
else:
   print "no hemos encotrado la clave deseada"

