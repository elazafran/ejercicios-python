'''
14. Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano.
La clave es la palabra en ingles y el valor es la palabra en castellano.
Se irán pidiendo por teclado la palabra en ingles y castellano hasta que digamos que no queremos continuar.
en caso de que exista la palabra en ingles se indicara que existe y cual es su significado en español
y finalmente se mostrara todo el diccionario.


'''
'''
diccionario = {}
articulos["raton"] = [25]
articulos["pendrive"] = [30]
articulos["ssd"] = [89]
articulos["teclado"] = [10]
articulos["pantalla"] = [150.0]


for articulo, precio in articulos.items():
   print articulo, ":", precio
print "Precios mayores a 100\n"
'''
diccionario = {}

while (True):
   clave= raw_input("introduzca palabra en ingles")
   valor= raw_input("introducca palabra en español")
   
   if(clave =="no" or valor=="no"):
      break
   else:
      if clave not in diccionario.keys():
         diccionario[clave]=valor
         print "añadimos"
      else:   
         print "NO añadimos"
print diccionario
