'''
15) Crear un diccionario en Python que defina como clave el número de documento de una persona
y como valor un string con su nombre.

Desarrollar las siguientes funciones:

1) Listado completo del diccionario.
2) Consulta del nombre de una persona ingresando su número de documento.

'''


diccionario = {}

while (True):
   clave= raw_input("introduzca numero de documento")
   valor= raw_input("introduzca su nombre")
   
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

'''
if clave in dicionario:
   print dicionario[nombre]
'''
